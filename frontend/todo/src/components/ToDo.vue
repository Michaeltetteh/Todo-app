<template>
       <div>
           <!-- <form>
            <input placeholder="Enter todo list name"
                v-model="name"
                class="input is-small" text="text" />
            <input placeholder="Enter todo list decription"
                v-model="description"
                class="input is-small" text="text" />
            <button type="submit" class="btn btn-primary"
                @click="addTodoList()">Submit</button>
           </form> -->

           <form @submit="addTodoList">
                <div class="row">
                    <div class="col">
                    <input v-model="name" type="text" class="form-control" placeholder="Enter todo list name">
                    </div>
                    <div class="col">
                    <input v-model="description" type="text" class="form-control" placeholder="Enter todo list decription">
                    </div>
                    <!-- <div class="col"> -->
                        <button class="btn btn-primary">Submit</button>
                    <!-- </div> -->
                </div>
                
            </form>
       </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
export default {
    name: "ToDo",
    data() {
        return {
            name: '',
            description: ''
        }
    },

    methods: {
        addTodoList(evt) {
            evt.preventDefault();
            this.$store.dispatch('addTodoList',{'name':this.name,'description':this.description});
            this.name = '';
            this.description = '';
        }
    }
}
</script>

<style scoped>

</style>