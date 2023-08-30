from rest_framework import serializers

from .models import CampoProposta, Proposta, ValorCampo


class PropostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposta
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        campos = instance.campos.all()
        valor_campos = instance.valorcampo_set.all()

        campos_data = []
        for campo in campos:
            valor_campo = valor_campos.filter(campo=campo).first()
            if valor_campo:
                campo_data = {
                    'campo_id': campo.id,
                    'campo_nome': campo.nome,
                    'tipo': campo.tipo,
                    'valor_texto': valor_campo.texto,
                    'valor_imagem': valor_campo.imagem.url if valor_campo.imagem else None,
                    'valor_arquivo': valor_campo.arquivo.url if valor_campo.arquivo else None,
                    'valor_booleano': valor_campo.booleano
                }
                campos_data.append(campo_data)

        representation['campos'] = campos_data
        return representation


class CampoPropostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampoProposta
        fields = '__all__'
    
class ValorCampoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValorCampo
        fields = ['campo', 'texto', 'imagem', 'arquivo', 'booleano']

class PropostaRegisterSerializer(serializers.ModelSerializer):
    campos_valores = ValorCampoSerializer(many=True, write_only=True)

    class Meta:
        model = Proposta
        fields = ['nome', 'campos_valores']

    def create(self, validated_data):
        campos_valores_data = validated_data.pop('campos_valores')
        proposta = Proposta.objects.create(**validated_data)

        for campo_valor_data in campos_valores_data:
            campo_id = campo_valor_data.pop('campo').id
            ValorCampo.objects.create(
                proposta=proposta,
                campo_id=campo_id,
                **campo_valor_data
            )

        return proposta

