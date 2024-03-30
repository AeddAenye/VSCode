<template>
  <div class="background">
    <div class="login">
      <div class="choosedomain">

      </div>
      <div class="page-name">
        <span>Войти в аккаунт</span>
      </div>
      <div class="emailfield">
        <div class="name">
          <input type="text" name="" class="emailtxt" v-model="name" placeholder="Имя почты"
            :class="{ 'error': inputerror, 'shake': shouldShake }">
        </div>
        <div class="domain">
          <select name="domainselect" v-model="domain" v-show="checkdomain()">
            <option value="mail">@mail.ru</option>
            <option value="yandex">@yandex.com</option>
            <option value="gmail">@gmail.com</option>
            <option value="yohoo">@yahoo.com</option>
          </select>
        </div>
      </div>
      <div class="password">
        <button type="button" @click="checkemail()">Ввести пароль</button>
        <form class="rememberme">
          <input type="checkbox">
          <label for="html">запомнить меня</label>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

let name = ref('')
let domain = ref('@mail.ru')
let inputerror = ref(false)
let shouldShake = ref(false);

const emailregex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/

let domainvisible = true


const checkdomain = () => {
  name.value.includes('@') ? domainvisible = false : domainvisible = true
  return domainvisible
}

const checkemail = () => {
  console.log("Мы зашли в блок checkemail");
  console.log(`name = ${name.value}, domainvisible=${domainvisible}`);

  if (domainvisible && name.value !== '' && /^[^\s@]+$/.test(name.value)) {
    console.log(1);
    alert(`Вариант 1, когда domainvisible=true\nВаш email ${name.value + domain.value}`)
  }
  else if (emailregex.test(name.value)) {
    console.log(2);
    alert(`Вариант 2, когда domainvisible=false\nВаш email ${name.value}`)
  }
  else {
    inputerror.value = true;
    shouldShake.value = true;

    setTimeout(() => {
      inputerror.value = false
      shouldShake.value = false
    }, 1000)
  }
}
</script>

<style scoped>
.background {
  background-color: rgba(0, 0, 0, 0.7);
  height: 100svh;
  width: 100svw;
}

.page-name {
  display: flex;
  justify-content: center;
  font-size: 1.2rem;
  margin: 10px;
  margin-bottom: 30px;
}

.login {
  width: 35svw;
  height: 70svh;
  border-radius: var(--br-radius);
  margin: 0 auto;
  padding: 20px 40px;
  background-color: white;
}

.emailfield {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.emailfield .name {
  width: 100%;
  display: flex;
  justify-content: center;

}

.emailfield input {
  width: 100%;
  padding: 10px;
  border-radius: var(--br-radius);
  font-size: 1.2rem;
  border: 2px solid;
  border-color: var(--br-color);

  transition: all 0.5s ease;
}

.emailfield input.error {
  border: 2px solid rgb(208, 0, 0);
  background-color: rgb(255, 111, 111);
}

.emailfield input.error::placeholder {
  color: white;
}

.emailfield input.shake {
  animation: shake 0.5s;
  /* Define the shake animation */
}

@keyframes shake {

  0%,
  100% {
    transform: translateX(0);
    /* Initial and final position, no translation */
  }

  10%,
  30%,
  50%,
  70%,
  90% {
    transform: translateX(-3px);
    /* Move left */
  }

  20%,
  40%,
  60%,
  80% {
    transform: translateX(3px);
    /* Move right */
  }
}


.emailfield .domain {
  font-size: 1.2rem;
  margin: 0px 10px;
}

select{
  border: none;
  font-size: 1.4rem;
  background-color: white;
}

select option{
  border: none;
}

.password {
  margin: 30px 0px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.rememberme {
  font-size: 1.1rem;
  display: flex;
  align-items: center;
}

input[type='checkbox'] {
  margin: 10px;
  width: 16px;
  height: 16px;
}

button {
  padding: 10px;
  font-size: 1.2rem;
  font-weight: 600;
  border: none;
  background-color: rgb(59, 59, 183);
  color: white;
  border-radius: var(--br-radius);
}
</style>
