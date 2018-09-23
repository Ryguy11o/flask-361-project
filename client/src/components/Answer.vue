<template>
	<div class="whole-element">
		<div class="card" @click="showParagraph">
			{{answer}}
		</div>
		<div class="paragraph" v-if="show_paragraph">
			{{paragraph}}
		</div>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	name: 'Answer',
	data() {
		return{
			paragraph: null,
			show_paragraph: false,
		}
	},	
	props: {
	  answer: {
	  	type: String,
	  	required: true,
	  }
	},
	methods: {
		getParagraph(){
			
			const data = {sentence: this.answer};
			const path = 'http://localhost:5000/getParagraph';

			axios.post(path, data)
			.then((res) => {
				let returned_list = res.data;
				this.paragraph = "";
				for (var i = 0; i < returned_list.length; i++){
					this.paragraph = this.paragraph + " " + returned_list[i];
				}
			})
			.catch((error) => {
				// eslint-disable-next-line
				console.error(error);
			});
		},

		showParagraph(){
			if(this.show_paragraph){
				this.show_paragraph = false;
			} else {
				if(this.paragraph != null){
					this.show_paragraph = true;
				} else {
					this.getParagraph();
				}
			}
		}
	},

	created() {
		this.getParagraph();
	}
}
</script>

<style scoped>
	.card {
		width: 100%;
		padding: 20px;
		margin-top: 10px;
		border-radius: 4px;
		background: #9C27B0;
		color: white;
	}

	.paragraph {
		width: 100%;
		padding: 20px;
		background: #FFF;
		text-align: left;
	}

	.card:hover {
		background:#7B1FA2;
		cursor: pointer;
	}

	.whole-element {
		margin-bottom: 10px;
	}
</style>