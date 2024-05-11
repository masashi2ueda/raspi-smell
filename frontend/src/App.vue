<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import { ref, onMounted } from 'vue'
import axios from 'axios'

const val = ref(0)
const interval = ref()

onMounted(() =>{
  interval.value = setInterval(() => {
    // axios.get('http://127.0.0.1:5053/')
    axios.get('smellpi:5053/sensor')
    .then(response =>{
      val.value = response.data.val
      // console.log(response.data.val);
    })
    // val.value += 1
  }, 1000);
})

</script>

<template>
  {{  val }}
</template>

<style scoped>
</style>
