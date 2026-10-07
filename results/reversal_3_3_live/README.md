# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-07 14:40:06 EDT`
Last processed slot: `manage_1430`

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

- Cash: `$53,034.30`
- Equity: `$106,109.30`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$962.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ABNB     option         option ABNB261120C00160000       2026-10-06                   1     55     52112.5                 53075.0         9.48           9.65      160.14        160.68          bid_ask_mid                       9.65                bid_ask_mid                    True           962.5                   1.85         83.33               12               2.4         42.26           42.16                  40.56                 310.0           20.0               0.06                      ok
```

## Today's Closed Trades (2026-10-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           93.33               15            1.27              0.28         31.01                26.61         0.538          pass              0.461              6.0                           0.218               -2.53             -0.207                                 ok            True                  False
  SNPS           82.50               40            0.53              1.86        504.37                54.22         0.528          pass              0.490             56.9                           0.439               21.66              2.337                                 ok            True                  False
  MPWR           80.00               15            3.42             35.28       1458.57                53.62         0.521          pass              0.138             17.4                           0.268                5.16              0.934                                 ok            True                  False
  NVDA           90.48               21            1.03              1.72        238.50                24.15         0.516          pass              0.438             11.2                           0.194                5.00              0.669                                 ok            True                  False
  UPRO           82.14               28            0.79              0.86        156.04                30.90         0.508          pass              0.418             63.3                           0.622                3.25              0.352                                 ok            True                  False
  DASH           82.14               28            1.59              2.16        192.70                42.81         0.502          pass              0.324             32.2                           0.546                0.67              0.206                                 ok            True                  False
  SOXL           79.17               24            4.81              5.53        161.89               111.15         0.602          pass              0.269             38.4                           0.481                6.91              1.241                                 ok           False                  False
  META           61.54               13            1.90              9.84        734.66                55.45         0.595          pass              0.150             23.3                           0.407               -2.59             -0.325            downtrend_blocked_slope           False                  False
   STX           88.57               35            0.78              4.40        803.75                69.91         0.562          pass              0.675             74.6                           0.508              -13.41             -1.289            downtrend_blocked_slope           False                  False
   CEG           86.11               36            0.46              0.97        299.98                58.89         0.545          pass              0.661             90.1                           0.766               13.31              1.075                                 ok           False                  False
  QCOM           78.95               19            2.63              3.33        179.60                56.22         0.545          pass              0.163             16.3                           0.371              -10.63             -1.105 downtrend_blocked_slope_and_streak           False                  False
  CSCO           89.19               37            0.14              0.11        117.89                34.67         0.519          pass              0.742             88.2                           0.609               11.09              1.123                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-10-07T12:00:04.521112-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:55:05.517664-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:50:05.710520-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:45:01.712221-04:00 early_entry_1145 early_entry_shadow      {"contract_symbol": "FTNT261120C00190000", "current_drop_pct": 0.59, "early_entry_score": 0.723, "early_reclaim_pct": 65.3, "entry_ask": 16.2, "entry_bid": 14.2, "entry_mode": "early", "entry_option_price": 15.2, "hypothetical_budget": 26517.15, "hypothetical_contracts": 17, "matched_signals": 42, "option_liquidity_status": "low_volume", "option_open_interest": 225.0, "option_spread_pct": 13.16, "option_volume": 11.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.68, "shadow_only": true, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.478, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.723, "early_reclaim_pct": 65.3, "matched_signals": 42, "recovery_stability_score": 0.68, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-07T11:40:04.680085-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:35:06.426609-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:30:05.653907-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:25:06.559799-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:20:05.827676-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:15:06.288558-04:00 early_entry_1115 early_entry_shadow {"contract_symbol": "FTNT261120C00190000", "current_drop_pct": 0.62, "early_entry_score": 0.716, "early_reclaim_pct": 63.1, "entry_ask": 15.75, "entry_bid": 14.2, "entry_mode": "early", "entry_option_price": 14.975, "hypothetical_budget": 26517.15, "hypothetical_contracts": 17, "matched_signals": 42, "option_liquidity_status": "low_volume", "option_open_interest": 225.0, "option_spread_pct": 10.35, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.724, "shadow_only": true, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.476, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.716, "early_reclaim_pct": 63.1, "matched_signals": 42, "recovery_stability_score": 0.724, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.476, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261007144006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261007144006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261007144006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261007144006)

</details>
