import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todoItem: []
  },
  mutations: {
      ADD_TODO_LIST(state, payload) {
        state.todoItem = payload
      }
  },
  actions: {
      getTodoItems({ commit }) {
        axios.get('http://localhost:8000/api/show/').then((res) => {
          commit('ADD_TODO_LIST', res.data)
        });
      },
  },
  getters: {
    todoItems: state => state.todoItem
  }
})
