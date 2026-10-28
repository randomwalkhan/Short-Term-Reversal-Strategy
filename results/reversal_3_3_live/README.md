# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-28 15:55:04 EDT`
Last processed slot: `manage_1600`

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

- Cash: `$64,409.30`
- Equity: `$130,109.30`
- Realized PnL: `$119,884.30`
- Unrealized PnL: `$225.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CSCO     option         option CSCO261218C00110000       2026-10-28                   0     90     65475.0                 65700.0         7.28            7.3      110.47        110.24          bid_ask_mid                        7.3                bid_ask_mid                    True           225.0                   0.34         80.77               26              0.82         42.92           43.87                  35.12                4095.0         1198.0               0.02                      ok
```

## Today's Closed Trades (2026-10-28)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM261218C00230000     32          2026-10-26         2026-10-28         20.0        19.1 -2880.0        -4.5 time_exit_at_4pm_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           91.67               12            0.83              0.36         62.19                25.51         0.602          pass              0.499             38.1                           0.539               -1.18             -0.104                                 ok            True                  False
  PAYX           80.00               15            0.69              0.53        109.03                35.39         0.585          pass              0.304             70.8                           0.819                1.14              0.328                                 ok            True                  False
   KHC           88.46               26            0.83              0.14         24.00                36.33         0.548          pass              0.537             50.0                           0.699                5.11              0.635                                 ok            True                  False
  CRWD           85.71               42            0.65              1.21        267.50                57.68         0.512          pass              0.583             59.7                           0.686                6.82              1.280                                 ok            True                  False
    ZS           90.00               30            1.67              3.04        258.85                56.99         0.512          pass              0.529             25.9                           0.363               15.86              2.319                                 ok            True                  False
   CEG           85.71               42            0.23              0.41        258.80                65.80         0.589          pass              0.672             87.0                           0.712               -7.57             -0.854 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           88.89                9            1.26              0.19         21.76                26.07         0.573          pass              0.377             27.6                           0.446                2.45              0.224                                 ok           False                  False
  MPWR           78.57               42            0.22              1.86       1211.09                59.51         0.553          pass              0.521             88.4                           0.765               -2.73             -0.569            downtrend_blocked_slope           False                  False
   ADP          100.00                3            2.52              5.17        290.89                27.84         0.547          pass              0.538             27.9                           0.644                1.93              0.445                                 ok           False                  False
  CSCO           76.19               21            1.06              0.83        111.02                35.12         0.544          pass              0.244             38.9                           0.367               -3.03             -0.034                                 ok           False                  False
   AEP           83.33                6            1.68              1.53        129.64                18.44         0.543          pass              0.155              3.9                           0.235                1.57              0.382                                 ok           False                  False
  META           80.00               20            1.34              5.81        617.70                37.09         0.541          pass              0.198             25.8                           0.377              -17.04             -2.027 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-10-28T15:50:06.462666-04:00      manage_1600                    exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"asset_type": "option", "contract_symbol": "TEAM261218C00230000", "fill_price": 19.1, "pnl": -2880.0, "reason": "time_exit_at_4pm_scan", "return_pct": -4.5, "ticker": "TEAM"}
2026-10-28T15:10:04.409011-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-10-28T15:05:05.708724-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-10-28T15:00:05.530535-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-10-28T14:55:06.400966-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-10-28T14:50:01.756543-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"allocated_cash": 65475.0, "asset_type": "option", "contract_symbol": "CSCO261218C00110000", "contracts": 90, "early_entry_score": 0.34, "entry_mode": "regular", "entry_option_price": 7.275, "execution_mode": "option", "matched_signals": 26, "option_liquidity_status": "ok", "option_open_interest": 4095.0, "option_spread_pct": 2.06, "option_volume": 1198.0, "success_rate": 80.77, "ticker": "CSCO", "timing_score": 0.533}
2026-10-28T14:50:01.756543-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"early_entry_score": 0.297, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 14.29, "option_volume": 11.0, "reason": "no_trade_low_option_liquidity", "ticker": "KHC", "timing_score": 0.562}
2026-10-28T14:50:01.756543-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-28", "training_samples": 6213, "window": 5}
2026-10-28T12:00:04.408643-04:00 early_entry_1200      early_entry_shadow   {"contract_symbol": "ALNY261218C00230000", "current_drop_pct": 0.6, "early_entry_score": 0.709, "early_reclaim_pct": 80.0, "entry_ask": 19.0, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 17.35, "hypothetical_budget": 34382.15, "hypothetical_contracts": 19, "matched_signals": 43, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 69.0, "option_spread_pct": 19.02, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.759, "shadow_only": true, "success_rate": 88.37, "ticker": "ALNY", "timing_score": 0.462, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.709, "early_reclaim_pct": 80.0, "matched_signals": 43, "recovery_stability_score": 0.759, "success_rate": 88.37, "ticker": "ALNY", "timing_score": 0.462, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-28T11:55:06.476667-04:00 early_entry_1155      early_entry_shadow {"contract_symbol": "ALNY261218C00230000", "current_drop_pct": 0.51, "early_entry_score": 0.726, "early_reclaim_pct": 83.1, "entry_ask": 19.0, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 17.35, "hypothetical_budget": 34382.15, "hypothetical_contracts": 19, "matched_signals": 44, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 69.0, "option_spread_pct": 19.02, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.776, "shadow_only": true, "success_rate": 88.64, "ticker": "ALNY", "timing_score": 0.461, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.726, "early_reclaim_pct": 83.1, "matched_signals": 44, "recovery_stability_score": 0.776, "success_rate": 88.64, "ticker": "ALNY", "timing_score": 0.461, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261028155504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261028155504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261028155504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261028155504)

</details>
