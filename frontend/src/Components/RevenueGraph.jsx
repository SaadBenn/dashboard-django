import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import Card from './Card';
import Graph from './Graph';
import { useSelector } from 'react-redux';

const RevenueGraph = ({ userId, loadRevenueData }) => {
  const data = useSelector(({ revenue }) => revenue[userId]);

  useEffect(() => {
    loadRevenueData(userId);
  }, [userId]);

  return (
    <div>
      {data && data.hasOwnProperty('revenue') ? (
        <Graph data={data.revenue}></Graph>
      ) : null}
    </div>
  );
};

export default RevenueGraph;
