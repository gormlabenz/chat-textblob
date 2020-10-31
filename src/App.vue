<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" />
    <p class=" text-6xl">Hello You</p>
    <HelloWorld class="" msg="Welcome to Your Vue.js App" />
    <div
      class="bg-purple text-white sm:bg-green md:bg-blue md:text-yellow lg:bg-red xl:bg-orange ..."
    >
      Test
    </div>
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";

export default {
  name: "App",
  components: {
    HelloWorld
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
