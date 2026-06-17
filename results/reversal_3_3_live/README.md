# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-17 11:10:02 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$13,363.25`
- Equity: `$27,133.25`
- Realized PnL: `$15,985.75`
- Unrealized PnL: `$1,147.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  DRAM     option         option DRAM260717C00069000       2026-06-16                   1     17     12622.5                 13770.0         7.43            8.1       68.52         70.63          bid_ask_mid                        8.1                bid_ask_mid                    True          1147.5                   9.09         90.91               11              3.59         94.78           89.14                 109.99                 846.0          111.0               0.06                      ok
```

## Today's Closed Trades (2026-06-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PAYX          100.00               22            0.51              0.36        100.13                31.37         0.600          pass              0.754             71.3                           0.422               -1.01              0.095                                 ok            True                  False
  UPRO           93.33               30            0.60              0.60        143.88                48.01         0.591          pass              0.661             37.7                           0.230               -5.03             -0.497                                 ok            True                  False
  MDLZ           94.44               18            1.03              0.45         61.96                20.23         0.552          pass              0.580             28.9                           0.399                0.72              0.222                                 ok            True                  False
    ZS           77.14               35            0.93              0.83        126.88               152.67         0.876          pass              0.433             59.7                           0.382               -6.19             -0.570 downtrend_blocked_slope_and_streak           False                  False
  INTU           79.55               44            0.25              0.48        280.78                99.11         0.708          pass              0.542             90.4                           0.604              -12.99             -1.450 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                3            1.03              0.17         23.73                25.54         0.698          pass              0.512             14.0                           0.205                5.37              0.808                                 ok           False                  False
   PEP          100.00                5            1.34              1.38        145.53                20.43         0.636          pass              0.533             23.2                           0.342                2.59              0.384                                 ok           False                  False
  MCHP           93.94               33            0.24              0.16         95.56                60.62         0.632          pass              0.804             72.0                           0.506               -1.61              0.141                                 ok           False                  False
   CSX          100.00                4            1.55              0.51         46.68                20.12         0.631          pass              0.481              5.8                           0.217                0.08              0.177                                 ok           False                  False
   XEL          100.00               27            0.01              0.01         78.98                23.22         0.590          pass              0.867             98.4                           0.537                2.18              0.284                                 ok           False                  False
   ADP           95.83               24            0.43              0.67        221.71                31.58         0.589          pass              0.762             70.0                           0.507               -3.66             -0.283            downtrend_blocked_slope           False                  False
   WMT           77.78               18            1.26              1.06        120.57                34.81         0.582          pass              0.130              6.2                           0.123                5.70              0.484                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-06-17T11:10:02.894138-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T11:05:03.233466-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T11:00:05.904410-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:55:04.940733-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:50:01.959639-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:45:01.979292-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:40:01.956283-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:35:06.928976-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:30:05.890992-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:25:01.204897-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260617111002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260617111002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260617111002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260617111002)

</details>
