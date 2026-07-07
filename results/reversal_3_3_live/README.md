# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-07 15:20:02 EDT`
Last processed slot: `manage_1530`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$13,056.75`
- Equity: `$26,421.75`
- Realized PnL: `$15,746.75`
- Unrealized PnL: `$675.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option CSX260821C00047500       2026-07-07                   0     54     12690.0                 13365.0         2.35           2.47       48.48         48.53          bid_ask_mid                       2.47                bid_ask_mid                    True           675.0                   5.32          91.3               23              0.68         28.35           30.69                  21.52                2967.0           20.0               0.09                      ok
```

## Today's Closed Trades (2026-07-07)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  AMAT     option         option AMAT260821C00600000      1          2026-07-06         2026-07-07       75.775     68.1975 -757.75       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  UPRO           93.33               15            1.95              1.97        143.56                55.41         0.595            pass              0.512             21.1                           0.161                0.34              0.531                                 ok            True                  False
   KDP          100.00               13            1.01              0.22         31.65                33.28         0.584            pass              0.594             38.5                           0.525                2.54              0.463                                 ok            True                  False
  PCAR           80.00               20            1.25              1.10        125.44                37.79         0.527            pass              0.263             47.8                           0.747                3.51              0.477                                 ok            True                  False
   CSX           91.67               24            0.60              0.21         48.72                21.52         0.524            pass              0.632             58.5                           0.539                5.01              0.619                                 ok            True                  False
  VRTX           93.33               15            1.44              5.32        527.31                27.95         0.520            pass              0.605             54.8                           0.331               11.82              1.318                                 ok            True                  False
  MNST          100.00               17            0.96              0.65         97.09                16.15         0.519            pass              0.630             43.8                           0.543                3.67              0.412                                 ok            True                  False
  CSCO           91.67               12            1.54              1.23        113.45                39.71         0.572            pass              0.435             17.9                           0.183               -7.32             -0.720 downtrend_blocked_slope_and_streak           False                  False
   TXN           80.00                5            3.98              8.45        299.88                69.17         0.535            pass              0.154             33.4                           0.355              -12.29             -0.739            downtrend_blocked_slope           False                  False
   ADI           62.50                8            3.41              9.29        384.85                61.47         0.511            pass              0.127             25.2                           0.197              -15.70             -1.300            downtrend_blocked_slope           False                  False
  FAST           85.71                7            2.10              0.71         48.01                20.37         0.493 below_threshold              0.258             18.8                           0.370                2.55              0.509                                 ok           False                  False
  ASML           83.33                6            5.03             64.25       1797.54                78.10         0.492 below_threshold              0.183             14.8                           0.151              -10.16             -0.287            downtrend_blocked_slope           False                  False
  QCOM           73.68               19            3.10              4.05        184.75                82.48         0.487 below_threshold              0.177             22.7                           0.169              -18.57             -1.810 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-07-07T15:10:01.115389-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-07-07T15:05:02.177767-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-07-07T15:00:05.200618-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-07-07T14:55:05.093959-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-07-07T14:50:02.270348-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"allocated_cash": 12690.0, "asset_type": "option", "contract_symbol": "CSX260821C00047500", "contracts": 54, "early_entry_score": 0.601, "entry_mode": "regular", "entry_option_price": 2.35, "execution_mode": "option", "matched_signals": 23, "option_liquidity_status": "ok", "option_open_interest": 2967.0, "option_spread_pct": 8.51, "option_volume": 20.0, "success_rate": 91.3, "ticker": "CSX", "timing_score": 0.525}
2026-07-07T14:50:02.270348-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"early_entry_score": 0.524, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 36.0, "option_spread_pct": 6.9, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "UPRO", "timing_score": 0.594}
2026-07-07T14:50:02.270348-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-07", "training_samples": 5385, "window": 5}
2026-07-07T12:00:06.141276-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 1.31, "early_entry_score": 0.792, "early_reclaim_pct": 68.2, "entry_ask": 16.35, "entry_bid": 15.45, "entry_mode": "early", "entry_option_price": 15.9, "hypothetical_budget": 12873.38, "hypothetical_contracts": 8, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 770.0, "option_spread_pct": 5.66, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.633, "shadow_only": true, "success_rate": 96.88, "ticker": "FTNT", "timing_score": 0.41, "top_candidates": [{"current_drop_pct": 1.31, "early_entry_score": 0.792, "early_reclaim_pct": 68.2, "matched_signals": 32, "recovery_stability_score": 0.633, "success_rate": 96.88, "ticker": "FTNT", "timing_score": 0.41, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-07T11:55:03.609525-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 1.31, "early_entry_score": 0.792, "early_reclaim_pct": 68.2, "entry_ask": 16.35, "entry_bid": 15.45, "entry_mode": "early", "entry_option_price": 15.9, "hypothetical_budget": 12873.38, "hypothetical_contracts": 8, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 770.0, "option_spread_pct": 5.66, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.675, "shadow_only": true, "success_rate": 96.88, "ticker": "FTNT", "timing_score": 0.41, "top_candidates": [{"current_drop_pct": 1.31, "early_entry_score": 0.792, "early_reclaim_pct": 68.2, "matched_signals": 32, "recovery_stability_score": 0.675, "success_rate": 96.88, "ticker": "FTNT", "timing_score": 0.41, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-07T11:50:02.135353-04:00 early_entry_1150      early_entry_shadow {"contract_symbol": "FTNT260807C00152500", "current_drop_pct": 0.95, "early_entry_score": 0.851, "early_reclaim_pct": 76.9, "entry_ask": 18.25, "entry_bid": 15.9, "entry_mode": "early", "entry_option_price": 17.075, "hypothetical_budget": 12873.38, "hypothetical_contracts": 7, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 125.0, "option_spread_pct": 13.76, "option_volume": 120.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.751, "shadow_only": true, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.4, "top_candidates": [{"current_drop_pct": 0.95, "early_entry_score": 0.851, "early_reclaim_pct": 76.9, "matched_signals": 37, "recovery_stability_score": 0.751, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.4, "trend_health_status": "ok"}, {"current_drop_pct": 0.77, "early_entry_score": 0.712, "early_reclaim_pct": 78.6, "matched_signals": 38, "recovery_stability_score": 0.697, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.363, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260707152002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260707152002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260707152002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260707152002)

</details>
