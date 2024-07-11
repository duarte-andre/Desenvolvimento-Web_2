<script setup lang="ts">
import { ref } from "vue";
const{signOut} = useAuth();




const logout = () => {
  signOut({redirect: false})
  .then(()=>{
    console.log("desvinculação realizada com sucesso!");
    navigateTo("/");
  })
  .catch(()=>{
      console.log("Falha ao realizar desvinculação :(")
  }); 
}

const redirectLogin = () => {
  navigateTo('/login');
};

const painel = ref();

const toggle = (event: any) => {
    painel.value.toggle(event);
}

</script>

<template>
  <header>
    <div class="flex align-items-center justify-content-center">
      <div class="user-icon" @click="redirectLogin">
        <i class="pi pi-user">   Login</i>
      </div>
        <div class="menu-item flex align-items-center justify-content-center mr-4">
          <i class="pi pi-bookmark-fill" style="margin-right: 8px;"></i>
          <NuxtLink to="/">Livros</NuxtLink>
        </div>
        <div class="menu-item flex align-items-center justify-content-center mr-4">
          <i class="pi pi-briefcase mr-1" style="margin-right: 8px;"></i>
          <NuxtLink to="/emprestimo">Emprestimos</NuxtLink>
        </div>
        <div class="menu-item flex align-items-center justify-content-center mr-4">
          <i class="pi pi-shopping-cart mr-1" style="margin-right: 8px;"></i>
          <NuxtLink to="/carrinho">Carrinho</NuxtLink>
        </div>
        <div class="menu-item flex align-items-center justify-content-center mr-4" @click="logout">
          <i class="pi pi-sign-out mr-1" style="margin-right: 8px;"></i>
          <span>Logout</span>
        </div>
        <div class="chatbot">
            <Button type="button" icon="pi pi-comment" label="Chatbot" @click="toggle" />
            <OverlayPanel ref="painel">
                <iframe allow="microphone;" width="350" height="430"
                    src="https://console.dialogflow.com/api-client/demo/embedded/8a73aba1-0c7d-4fe9-90ce-7478e59304d1">
                </iframe>
            </OverlayPanel>
         </div>
    </div>
  </header>
</template>

<style scoped lang="scss">
header {
  width: 100vw;
  height: var(--altura-header);
  border: 1px solid #ccc; /* Adiciona uma borda */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Adiciona uma sombra */
  
  

  .menu-item{
    height: var(--altura-header);
    

    
    a{
      text-decoration: none;
      color: black;
    }
    &:hover{
      transform: scale(1.1);
    }
  }
  .chatbot {
    position: absolute;
    top: 4.5%;
    right: 30px; /* Ajuste a distância da borda direita conforme necessário */
    transform: translateY(-50%); /* Para centralizar verticalmente */
  }
  .user-icon {
  position: absolute;
  top: 4.5%;
  left: 30px; /* Ajuste a distância da borda direita conforme necessário */
  transform: translateY(-50%); /* Para centralizar verticalmente */
  // border: 2px solid black; /* Adiciona uma borda mais larga */
  // border-radius: 5px; /* Define o raio da borda para deixá-la arredondada */
  // padding: 5px; /* Adiciona preenchimento ao redor do ícone */
  cursor: pointer;
}

}


</style>
