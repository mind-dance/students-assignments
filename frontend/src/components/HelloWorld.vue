<template>
  <div>
    <button @click="fetchWelcomeMessage">获取欢迎消息</button>
    <p>{{ welcomeMessage }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const welcomeMessage = ref('');
async function fetchWelcomeMessage() {
  const response = await axios.get('http://localhost:5000/api/welcome')
  // if (!response.ok) {
  //   alert(`HTTP error! status: ${response.status}`);
  //   return;
  // }
  welcomeMessage.value = await response.data.message
}
</script>
