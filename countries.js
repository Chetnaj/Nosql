
const express = require('express')
const router = express.Router()

const CountryModel = require('../models/Country')

router.get('/',async (request, response) => {
    const countries = await CountryModel.find().populate('continent');
    response.status(200).json(countries);
});

router.get('/:id',async (request, response) => {
    const countryId = request.params.id;
    const countries = await CountryModel.findOne({
        _id: countryId
    });
    response.status(200).json(countries)
});

router.post('/',async (request, response) => {
    const {name, isoCode} = request.body

    const country = await CountryModel.create({
        name: name,
        isoCode 
    });

    response.status(200).json(country);
});

router.delete('/:id', async (request, response) =>{
    const countryId = request.params.id;

    await CountryModel.findOneAndDelete({
        _id: countryId
    });

    response.status(200).json({msg: 'Country well deleted !'});

});

router.put('/:id', async (request, response) =>{
    const countryId = request.params.id;
    const {name, isoCode} = request.body

    const country = await CountryModel.findOneAndUpdate({
        _id: countryId
    },{
        name,
        isoCode
    },{
        new: true
    });

    response.status(200).json(country);
     
});

//##1
router.get("/search/:query?",async (req, res)=>{
    const query = req.params.query;
    const result = await CountryModel.find({
        name: {$regex: query,$options: "i"}
    });
    res.status(200).json(result);
})

//##2
router.get('/all/bypop',async (req, res)=>{
    const countries = await CountryModel.find()
    .sort({population: 1});
    res.status(200).json(countries);
});

//##6

router.get('', async (req,res) => {
    const countries = await CountryModel.find().sort({population: 1})
        res.status(200).json(countries);
});


//##7
router.get('', async (req,res) => {
    const countries = await CountryModel.find({
        name: {$regex : new RegExp(".*u.*","i")},
        population:{ $gte: 30000}},
        ['name','isocode','population'] )
        .populate('continent','')
    })

module.exports = router;