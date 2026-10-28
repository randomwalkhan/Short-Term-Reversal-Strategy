# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-28 15:10:04 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$3,289.30`
- Equity: `$131,424.30`
- Realized PnL: `$122,764.30`
- Unrealized PnL: `$-1,340.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CSCO     option         option CSCO261218C00110000       2026-10-28                   0     90     65475.0                 66375.0         7.28           7.38      110.47        110.18          bid_ask_mid                       7.38                bid_ask_mid                    True           900.0                   1.37         80.77               26              0.82         42.92           45.14                  35.12                4095.0         1198.0               0.02                      ok
  TEAM     option         option TEAM261218C00230000       2026-10-26                   2     32     64000.0                 61760.0        20.00          19.30      220.60        220.40          bid_ask_mid                      19.30                bid_ask_mid                    True         -2240.0                  -3.50        100.00               12              3.08         70.90           70.82                  47.89                 302.0           39.0               0.10                      ok
```

## Today's Closed Trades (2026-10-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           91.43               35            0.81              0.80        141.06                70.33         0.608            pass              0.707             58.1                           0.465               -2.08             -0.134                                 ok            True                  False
   KHC           83.33               18            1.48              0.25         23.95                36.33         0.555            pass              0.231             11.3                           0.150                4.43              0.606                                 ok            True                  False
  CTSH           94.59               37            0.55              0.26         66.11                50.77         0.533            pass              0.806             61.2                           0.322                5.42              0.568                                 ok            True                  False
    ZS           90.00               30            1.58              2.87        258.92                56.99         0.524            pass              0.461              2.8                           0.205               15.97              2.323                                 ok            True                  False
  MCHP           92.00               25            1.55              0.87         79.80                42.57         0.516            pass              0.597             41.9                           0.290               10.78              0.793                                 ok            True                  False
  ORLY           95.00               20            1.17              0.74         89.50                20.98         0.516            pass              0.554             11.8                           0.201                2.40              0.253                                 ok            True                  False
   LIN           83.33               24            0.57              2.02        507.78                14.39         0.500 below_threshold              0.363             43.8                           0.276                2.65              0.315                                 ok            True                  False
  TMUS           80.00               25            0.89              0.92        146.44                63.84         0.658            pass              0.366             66.8                           0.466               -7.78             -0.938            downtrend_blocked_slope           False                  False
  MDLZ           87.50                8            1.20              0.53         62.12                25.51         0.601            pass              0.292             10.7                           0.173               -1.55             -0.121           downtrend_blocked_streak           False                  False
   CEG           83.78               37            0.57              1.03        258.54                65.80         0.597            pass              0.544             67.7                           0.408               -7.88             -0.869 downtrend_blocked_slope_and_streak           False                  False
  MPWR           72.73               33            0.78              6.63       1209.05                59.51         0.567            pass              0.386             58.8                           0.366               -3.27             -0.595            downtrend_blocked_slope           False                  False
 CMCSA           85.71                7            1.58              0.24         21.74                26.07         0.564            pass              0.229              6.8                           0.126                2.11              0.209                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-10-28T15:10:04.409011-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-10-28T15:05:05.708724-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-10-28T15:00:05.530535-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-10-28T14:55:06.400966-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-10-28T14:50:01.756543-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"allocated_cash": 65475.0, "asset_type": "option", "contract_symbol": "CSCO261218C00110000", "contracts": 90, "early_entry_score": 0.34, "entry_mode": "regular", "entry_option_price": 7.275, "execution_mode": "option", "matched_signals": 26, "option_liquidity_status": "ok", "option_open_interest": 4095.0, "option_spread_pct": 2.06, "option_volume": 1198.0, "success_rate": 80.77, "ticker": "CSCO", "timing_score": 0.533}
2026-10-28T14:50:01.756543-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"early_entry_score": 0.297, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 14.29, "option_volume": 11.0, "reason": "no_trade_low_option_liquidity", "ticker": "KHC", "timing_score": 0.562}
2026-10-28T14:50:01.756543-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-28", "training_samples": 6213, "window": 5}
2026-10-28T12:00:04.408643-04:00 early_entry_1200      early_entry_shadow   {"contract_symbol": "ALNY261218C00230000", "current_drop_pct": 0.6, "early_entry_score": 0.709, "early_reclaim_pct": 80.0, "entry_ask": 19.0, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 17.35, "hypothetical_budget": 34382.15, "hypothetical_contracts": 19, "matched_signals": 43, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 69.0, "option_spread_pct": 19.02, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.759, "shadow_only": true, "success_rate": 88.37, "ticker": "ALNY", "timing_score": 0.462, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.709, "early_reclaim_pct": 80.0, "matched_signals": 43, "recovery_stability_score": 0.759, "success_rate": 88.37, "ticker": "ALNY", "timing_score": 0.462, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-28T11:55:06.476667-04:00 early_entry_1155      early_entry_shadow {"contract_symbol": "ALNY261218C00230000", "current_drop_pct": 0.51, "early_entry_score": 0.726, "early_reclaim_pct": 83.1, "entry_ask": 19.0, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 17.35, "hypothetical_budget": 34382.15, "hypothetical_contracts": 19, "matched_signals": 44, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 69.0, "option_spread_pct": 19.02, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.776, "shadow_only": true, "success_rate": 88.64, "ticker": "ALNY", "timing_score": 0.461, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.726, "early_reclaim_pct": 83.1, "matched_signals": 44, "recovery_stability_score": 0.776, "success_rate": 88.64, "ticker": "ALNY", "timing_score": 0.461, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-28T11:50:06.101583-04:00 early_entry_1150      early_entry_shadow   {"contract_symbol": "ALNY261218C00230000", "current_drop_pct": 0.65, "early_entry_score": 0.697, "early_reclaim_pct": 78.4, "entry_ask": 19.0, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 17.35, "hypothetical_budget": 34382.15, "hypothetical_contracts": 19, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 69.0, "option_spread_pct": 19.02, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.755, "shadow_only": true, "success_rate": 88.1, "ticker": "ALNY", "timing_score": 0.465, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.697, "early_reclaim_pct": 78.4, "matched_signals": 42, "recovery_stability_score": 0.755, "success_rate": 88.1, "ticker": "ALNY", "timing_score": 0.465, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261028151004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261028151004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261028151004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261028151004)

</details>
