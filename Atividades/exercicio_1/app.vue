<template>
  <div>
    <h1>Testando o CustomInput</h1>
    <!-- Início do componente CustomSelect -->
    <div class="custom-select">
      <label for="select">Escolha uma opção:</label>
      <!-- O select que exibirá as opções -->
      <select id="select" v-model="selectedOption" @change="handleChange">
        <!-- Iteração sobre as opções disponíveis -->
        <option v-for="(option, index) in selectOptions" :key="index" :value="option.value">{{ option.label }}</option>
      </select>
    </div>
    <!-- Exibição da opção selecionada -->
    <p>Opção Selecionada: {{ selectedOption }}</p>
    <!-- Fim do componente CustomSelect -->
  </div>
</template>

<script>
export default {
  data() {
    return {
      // Opções disponíveis para seleção no select
      selectOptions: [
        { label: 'Instagram', value: 'Instagram' },
        { label: 'Whatsapp', value: 'Whatsapp' },
        { label: 'Facebook', value: 'Facebook' }
      ],
      // Opção atualmente selecionada
      selectedOption: ''
    };
  },
  methods: {
    // Método chamado quando o valor selecionado é alterado
    handleChange() {
      console.log('Opção Selecionada:', this.selectedOption);
    }
  }
};
</script>

<style scoped lang="scss">
/* Estilos do componente CustomSelect */
.custom-select {
  margin-bottom: 20px;

  /* Estilos da label */
  label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
  };

  /* Estilos do select */
  select {
    width: 25%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
    outline: none; /* Remove a borda ao focar */
    transition: border-color 0.3s;

    /* Estilos quando o select está em foco */
    &:focus {
      border-color: dodgerblue; /* Altera a cor da borda ao focar */
    }
  }
}
</style>
