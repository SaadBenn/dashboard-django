import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import RevenueGraph from '../Components/RevenueGraph';
import { loadRevenueData } from '../actions';

const Container = ({ userId, revenue, loadRevenueData }) => {
  return (
    <RevenueGraph
      revenue={revenue}
      userId={userId}
      loadRevenueData={loadRevenueData}
    />
  );
};

const mapStateToProps = ({ revenue }) => {
  return {
    revenue,
  };
};

export default connect(mapStateToProps, {
  loadRevenueData,
})(Container);
