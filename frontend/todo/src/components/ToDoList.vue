<template>
    <div id="todo-list-container">
        <p>Your ToDo LIST </p>
        <div 
          v-for="obj in todoItems.data"
          :key="obj.index"
          class="card"
          id="todo-list">
          <div class="card-header">
            {{ obj.name }}
          </div>
          <div class="card-body" id="todo-body">
            {{ obj.description }}<br>
            <span class="badge badge-success">{{ obj.created_at }}</span>
          </div>
          <button type="button" class="btn btn-primary"
            @click="deleteTodoItem(obj)">Delete</button>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: "TodoList",
  created () {
    this.$store.dispatch('getTodoItems');
  },
  computed: {
    ...mapGetters([
      'todoItems'
    ])
  },

  methods: {
    ...mapActions([
      'deleteTodoItem'
    ])
  }
};
</script>

<style scoped>
#todo-list {
  margin-bottom: 5px;
  padding: 2px;

}

#todo-list-container {
  padding: 1px;
}
#todo-body {
  text-align: justify;
}
</style>