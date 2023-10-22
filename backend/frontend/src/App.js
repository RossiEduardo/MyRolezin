import React, { Component } from "react";
import './App.css';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import Button from '@mui/material/Button';
import axios from 'axios';



class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
		user_preference_music: '',
		user_preference_drink: '',
		user_preference_hour: '',
		user_preference_price: '',
	};
  }
  	

	enviarDadosParaBackend() {
		axios.get('/filter')
		.then(function (response) {
			console.log('Dados recebidos com sucesso:', response.data);
		// Faça algo com os dados recebidos, por exemplo, atualize o estado do componente
		})
		.catch(function (error) {
			console.error('Erro ao buscar dados:', error);
		});
	}


	render() {
		const roles = [
			{nome: 'tusca', value: 80},
			{nome: 'oktoberim',value: 50},
			{nome:'ies',value: 70},
			{nome:'show do thiaginho', value:75},
			{nome:'bailao', value: 65},
		]
		console.log(this.state.user_preference_drink)

		return (
			<div className="home-container">
				<h1>MyRolezin</h1>
				<h2> User preferences:</h2>
				<Box sx={{ minWidth: 120 }}>
					<FormControl fullWidth>
						<InputLabel id="demo-simple-select-label">Music</InputLabel>
						<Select
							labelId="demo-simple-select-label"
							id="demo-simple-select"
							value={this.state.user_preference_music}
							label="Music Type"
							onChange={(event) => this.setState({
								user_preference_music: event.target.value 
							})}
						>
							<MenuItem value={'Eletronic'}>Eletronic</MenuItem>
							<MenuItem value={'Pagode'}>Pagode</MenuItem>
							<MenuItem value={'Samba'}>Samba</MenuItem>
							<MenuItem value={'Rock'}>Rock</MenuItem>
							<MenuItem value={'Sertanejo'}>Sertanejo</MenuItem>
						</Select>
					</FormControl>
				</Box>
				<Box sx={{ minWidth: 120 }}>
					<FormControl fullWidth>
						<InputLabel id="demo-simple-select-label">Drink</InputLabel>
						<Select
							labelId="demo-simple-select-label"
							id="demo-simple-select"
							value={this.state.user_preference_drink}
							label="Drink Type"
							onChange={(event) => this.setState({
								user_preference_drink: event.target.value 
							})}
						>
							<MenuItem value={'Open Bar<'}>Open Bar</MenuItem>
							<MenuItem value={'Cerveja'}>Cerveja</MenuItem>
							<MenuItem value={'Vodka'}>Vodka</MenuItem>
							<MenuItem value={'Soda'}>Soda</MenuItem>
							<MenuItem value={'Juice'}>Juice</MenuItem>
						</Select>
					</FormControl>
				</Box>
				<Box sx={{ minWidth: 120 }}>
					<FormControl fullWidth>
						<InputLabel id="demo-simple-select-label">Hour</InputLabel>
						<Select
							labelId="demo-simple-select-label"
							id="demo-simple-select"
							value={this.state.user_preference_hour}
							label="Hour Type"
							onChange={(event) => this.setState({
								user_preference_hour: event.target.value 
							})}
						>
							<MenuItem value={'Afternoon'}>Afternoon</MenuItem>
							<MenuItem value={'Night'}>Night</MenuItem>
							<MenuItem value={'Mid Night'}>Mid Night</MenuItem>
						</Select>
					</FormControl>
				</Box>
				<Box sx={{ minWidth: 120 }}>
					<FormControl fullWidth>
						<InputLabel id="demo-simple-select-label">Price</InputLabel>
						<Select
							labelId="demo-simple-select-label"
							id="demo-simple-select"
							value={this.state.user_preference_price}
							label="Price Type"
							onChange={(event) => this.setState({
								user_preference_price: event.target.value 
							})}
						>
							<MenuItem value={'20 - 50'}>20 - 50</MenuItem>
							<MenuItem value={'50 - 100'}>50 - 100</MenuItem>
							<MenuItem value={'100 - 200'}>100 - 200</MenuItem>
							<MenuItem value={'200 +'}>200 +</MenuItem>
						</Select>
					</FormControl>
				</Box>
				<div className="save-button">
				<Button
					variant="contained"
					onClick={() => {
						this.enviarDadosParaBackend()
					}}
					style={{width: '200px'}}
				>
					Save
				</Button>
				</div>
				
				<h2> Your 'Rolezinsss': </h2>
				{roles.map((item, index) => (
					<div className="party-container" key={index}>
						
						{item.value >= 60 && 
							<React.Fragment>
								<div className="party-title"> <h3> {item.nome} </h3> </div>
								<div className="party-img"></div>
								<div className="party-description">ekodeokfoekofkeofoefeofkeok</div>
								<div className="party-relevant">{item.value}%</div>
							</React.Fragment>
						}
					</div>
				))}
			</div>
		)
	}
}


export default App;