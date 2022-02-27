const { response } = require('express');
const express = require('express')
const router = express.Router()

const ContinentModel = require('../models/Continent')

router.get('/',async (req, res) => {
    const continents = await ContinentModel.find();
    res.status(200).json(continents);
});

//##3
router.get('/number',async (req, res)=>{
    const countries = await ContinentModel.aggregate([{
        $addFields: {count: {$size:"countries"}}
 }]);
 res.status(200).json(continents);
})
 //##4
router.get('/firstfour', async(req,res)=> {
    const fourth = await ContinentModel.find().populate({
        path: 'countries'
    }, null,{sort: 'name',limit: 4});
    res.status(200).json(fourth);
});


module.exports = router;