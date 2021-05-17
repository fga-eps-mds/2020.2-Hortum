# Generated by Django 3.1.7 on 2021-05-12 16:54

from django.db import migrations, models
import django.db.models.deletion
import hortum.announcement.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=30)),
                ('type_of_product', models.CharField(choices=[('Frangos Caipira', 'Frangos Caipira'), ('Galinhas poedeiras', 'Galinhas poedeiras'), ('Ovos de Galinha', 'Ovos de Galinha'), ('Ovos férteis', 'Ovos férteis'), ('Licor', 'Licor'), ('Suco', 'Suco'), ('Vinho', 'Vinho'), ('Carne suína', 'Carne suína'), ('Carne Caprina/Ovina', 'Carne Caprina/Ovina'), ('Carne de Frango', 'Carne de Frango'), ('Carne de Outras Aves', 'Carne de Outras Aves'), ('Peixes', 'Peixes'), ('Cogumelos em Conserva', 'Cogumelos em Conserva'), ('Champignon', 'Champignon'), ('Cogumelo Hiratake', 'Cogumelo Hiratake'), ('Cogumelo Hiratake Salmão', 'Cogumelo Hiratake Salmão'), ('Cogumelo Shimeji', 'Cogumelo Shimeji'), ('Mandioca Descascada Congelada', 'Mandioca Descascada Congelada'), ('Polpa de frutas', 'Polpa de frutas'), ('Pratos congelados', 'Pratos congelados'), ('Sorvetes', 'Sorvetes'), ('Açúcar Mascavo', 'Açúcar Mascavo'), ('Melado', 'Melado'), ('Rapadura', 'Rapadura'), ('Farinha de Mandioca', 'Farinha de Mandioca'), ('Farinha de Tapioca', 'Farinha de Tapioca'), ('Massa de Tapioca', 'Massa de Tapioca'), ('Massa para Bolos', 'Massa para Bolos'), ('Hibiscus', 'Hibiscus'), ('Hortaliças', 'Hortaliças'), ('Plantas Aromáticas', 'Plantas Aromáticas'), ('Doce de Corte', 'Doce de Corte'), ('Doce Pastoso', 'Doce Pastoso'), ('Agave', 'Agave'), ('Areca bambu', 'Areca bambu'), ('Arnica', 'Arnica'), ('Áster', 'Áster'), ('Azaléia', 'Azaléia'), ('Babosa', 'Babosa'), ('Bambu', 'Bambu'), ('Begônia - Vaso', 'Begônia - Vaso'), ('Boldo', 'Boldo'), ('Bromélias', 'Bromélias'), ('Buxinho', 'Buxinho'), ('Cactos/suculentas', 'Cactos/suculentas'), ('Citronela', 'Citronela'), ('Cróton', 'Cróton'), ('Dracena', 'Dracena'), ('Fenix', 'Fenix'), ('Ficus - Folhagem', 'Ficus - Folhagem'), ('Brinco de princesa', 'Brinco de princesa'), ('Capuchinha', 'Capuchinha'), ('Gerânio comum', 'Gerânio comum'), ('Heliconias', 'Heliconias'), ('Jurubeba', 'Jurubeba'), ('Lavanda', 'Lavanda'), ('Liriopsis', 'Liriopsis'), ('Margarida', 'Margarida'), ('Moréia', 'Moréia'), ('Moringa', 'Moringa'), ('Mudas Frutíferas', 'Mudas Frutíferas'), ('Mudas Nativas', 'Mudas Nativas'), ('Murta', 'Murta'), ('Orquídeas - Catlleya', 'Orquídeas - Catlleya'), ('Palmeiras em geral', 'Palmeiras em geral'), ('Pata de elefante', 'Pata de elefante'), ('Plantas medicinais , aromáticas e condimentares', 'Plantas medicinais , aromáticas e condimentares'), ('Primavera - bouganville', 'Primavera - bouganville'), ('Rosa - Corte', 'Rosa - Corte'), ('Rosa do deserto', 'Rosa do deserto'), ('Samambaia americana', 'Samambaia americana'), ('Tango', 'Tango'), ('Vinagreira', 'Vinagreira'), ('Abacate', 'Abacate'), ('Abacaxi', 'Abacaxi'), ('Acerola', 'Acerola'), ('Amora', 'Amora'), ('Banana', 'Banana'), ('Caju', 'Caju'), ('Cará', 'Cará'), ('Carambola', 'Carambola'), ('Coco', 'Coco'), ('Figo', 'Figo'), ('Framboesa', 'Framboesa'), ('Goiaba', 'Goiaba'), ('Graviola', 'Graviola'), ('Jabuticaba', 'Jabuticaba'), ('Jaca', 'Jaca'), ('Laranja', 'Laranja'), ('Limão', 'Limão'), ('Mamão', 'Mamão'), ('Manga', 'Manga'), ('Maracujá', 'Maracujá'), ('Melancia', 'Melancia'), ('Morango', 'Morango'), ('Pitaia', 'Pitaia'), ('Pitanga', 'Pitanga'), ('Tamarindo', 'Tamarindo'), ('Tangerina', 'Tangerina'), ('Uva', 'Uva'), ('Amendoim', 'Amendoim'), ('Arroz', 'Arroz'), ('Café', 'Café'), ('Milho', 'Milho'), ('Soja', 'Soja'), ('Feijão', 'Feijão'), ('Abóbora', 'Abóbora'), ('Açafrão da terra', 'Açafrão da terra'), ('Acelga', 'Acelga'), ('Couve Chinesa', 'Couve Chinesa'), ('Agrião', 'Agrião'), ('Alface', 'Alface'), ('Algodão', 'Algodão'), ('Alho', 'Alho'), ('Almeirão', 'Almeirão'), ('Batata', 'Batata'), ('Batata-doce', 'Batata-doce'), ('Berinjela', 'Berinjela'), ('Beterraba', 'Beterraba'), ('Brócolis', 'Brócolis'), ('Cebola', 'Cebola'), ('Cebolinha', 'Cebolinha'), ('Cenoura', 'Cenoura'), ('Chicória', 'Chicória'), ('Chuchu', 'Chuchu'), ('Coentro', 'Coentro'), ('Couve', 'Couve'), ('Couve-flor', 'Couve-flor'), ('Ervilha', 'Ervilha'), ('Espinafre', 'Espinafre'), ('Feijão-de-corda', 'Feijão-de-corda'), ('Gengibre', 'Gengibre'), ('Hibiscus', 'Hibiscus'), ('Hortelã', 'Hortelã'), ('Inhame', 'Inhame'), ('Jiló', 'Jiló'), ('Mandioca', 'Mandioca'), ('Maxixe', 'Maxixe'), ('Milho-verde', 'Milho-verde'), ('Mostarda', 'Mostarda'), ('Ora pro nobis', 'Ora pro nobis'), ('Iogurte', 'Iogurte'), ('Queijo', 'Queijo'), ('Leite', 'Leite'), ('Biscoitos', 'Biscoitos'), ('Bolos', 'Bolos'), ('Pães', 'Pães'), ('Salgados', 'Salgados'), ('Artesanato', 'Artesanato'), ('Abelhas', 'Abelhas'), ('Animais Ornamentais', 'Animais Ornamentais'), ('Composto orgânico Bokashi', 'Composto orgânico Bokashi'), ('Esterco de gado', 'Esterco de gado'), ('Café', 'Café'), ('Cabritas/Cabritos', 'Cabritas/Cabritos'), ('Damasco', 'Damasco'), ('Defumado de Suínos', 'Defumado de Suínos'), ('Farinha de Trigo', 'Farinha de Trigo'), ('Linguiça artesanal e defumados', 'Linguiça artesanal e defumados'), ('Potros/Potras', 'Potros/Potras'), ('Cana-de-açúcar', 'Cana-de-açúcar'), ('Feno', 'Feno'), ('Geléias', 'Geléias'), ('Pepino', 'Pepino'), ('Pimenta', 'Pimenta'), ('Pimentão', 'Pimentão'), ('Quiabo', 'Quiabo'), ('Rabanete', 'Rabanete'), ('Repolho', 'Repolho'), ('Rúcula', 'Rúcula'), ('Salsa', 'Salsa'), ('Tomate', 'Tomate'), ('Mel', 'Mel'), ('Extrato de Tomate', 'Extrato de Tomate'), ('Molho de Pimenta', 'Molho de Pimenta'), ('Carneiros', 'Carneiros'), ('Cordeiros/Cordeiras', 'Cordeiros/Cordeiras'), ('Eucalipto', 'Eucalipto'), ('Leitoes/Leitoas', 'Leitoes/Leitoas'), ('Outros', 'Outros')], default='Outros', max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0.0)),
                ('inventory', models.BooleanField(default=True)),
                ('publicationDate', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-publicationDate'],
            },
        ),
        migrations.CreateModel(
            name='Localization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=100)),
                ('idAnnoun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='localizations', to='announcement.announcement')),
            ],
        ),
        migrations.CreateModel(
            name='AnnouncementImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(null=True, upload_to=hortum.announcement.models.AnnouncementImage.upload_image_announ)),
                ('idImage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='announcement.announcement')),
            ],
        ),
    ]
