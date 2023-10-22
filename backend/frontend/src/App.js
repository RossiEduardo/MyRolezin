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
		roles: []
	};
  }
  
	// const [rolesTest, setRoles] =  useState({})
	// const [count, setCount] = useState(0);
  	

	enviarDadosParaBackend() {
		const params = {
			music: this.state.user_preference_music,
			drink: this.state.user_preference_drink,
			hour: this.state.user_preference_hour,
			price: this.state.user_preference_price	
		  };

		  axios.get('http://127.0.0.1:8000/filter', { params })
		  .then((response) => {
			console.log('Dados recebidos com sucesso:', response.data);
			this.setState({ roles: response.data });
			// setRoles(response.data)
			// return response.data
			// Faça algo com os dados recebidos, por exemplo, atualize o estado do componente
		  })
		  .catch((error) => {
			console.error('Erro ao buscar dados:', error);
		  });
	}


	render() {
		let roles = this.state.roles
		console.log('rolezin: ' + roles)
		

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
						roles = this.enviarDadosParaBackend()
					}}
					style={{width: '200px'}}
				>
					Save
				</Button>
				</div>
				
				<h2> Your 'Rolezinsss': </h2>
				{roles.map((item, index) => (
					<div className="party-container" key={index}>
						{item.score >= 0.1 && 
							<React.Fragment>
								<div className="party-title"> <h3> {item.name} </h3> </div>
								<div className="party-img"></div>
								<div className="party-description">{item.description}</div>
								<div className="party-relevant"><h4>My Score:</h4>{item.score}%</div>
							</React.Fragment>
						}
					</div>
				))}
			</div>
		)
	}
}


export default App;