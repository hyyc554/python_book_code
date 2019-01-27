new Vue({
    el:"#vue-app",
    data() {
        return {
            name:"hyc"
        }
    },
    methods: {
        greet:function(time){
            return "good" +" "+time+" "+ this.name;
        },
    },
});

