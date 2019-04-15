# Agenda RU UFSM 
Script para agendar automaticamente o Restaurante Universitário da Universidade Federal de Santa Maria. Muito útil para automatizar agendamentos com cronjobs.

### Configuração
Para configurar, basta editar o código fonte do script. As variáveis de configuração são:

- matricula: matrícula do usuário
- senha: senha do usuário no portal
- ru: restaurante onde se dará o almoço
- refeições: Lista com as refeições a serem agendadas
- modo: Quantos dias a partir da data devem ser agendados. Usar "semanal" para a semana inteira, qualquer outra coisa para apenas o dia seguinte

### Automatização
Para automatizar o script, basta adicioná-lo como um serviço cron. 

### Desenvolvimento
Feel free to PR :)

### Licença
BSD 2-clause simple license.
