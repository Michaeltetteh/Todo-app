<template>
  <div id="app">
    <div class="container">
      <ToDo />
      <ToDoList />
    </div>
  </div>
</template>

<script>
import ToDo from './components/ToDo.vue'
import ToDoList from './components/ToDoList.vue'

export default {
  name: 'App',
  components: {
    ToDo,
    ToDoList
  }
}
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
