# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-17 11:00:05 EDT`
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
- Equity: `$27,515.75`
- Realized PnL: `$15,985.75`
- Unrealized PnL: `$1,530.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  DRAM     option         option DRAM260717C00069000       2026-06-16                   1     17     12622.5                 14152.5         7.43           8.32       68.52         70.42          bid_ask_mid                       8.32                bid_ask_mid                    True          1530.0                  12.12         90.91               11              3.59         94.78           93.58                 109.99                 846.0          111.0               0.06                      ok
```

## Today's Closed Trades (2026-06-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PAYX          100.00               20            0.77              0.54        100.05                31.37         0.597          pass              0.696             56.5                           0.374               -1.27              0.083                                 ok            True                  False
  MDLZ           95.65               23            0.87              0.38         61.99                20.23         0.527          pass              0.659             40.0                           0.621                0.88              0.230                                 ok            True                  False
    ZS           76.47               34            1.17              1.04        126.78               152.67         0.871          pass              0.395             49.3                           0.297               -6.42             -0.581 downtrend_blocked_slope_and_streak           False                  False
  INTU           78.05               41            0.52              1.02        280.55                99.11         0.708          pass              0.510             79.8                           0.483              -13.23             -1.462 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                3            0.88              0.15         23.74                25.54         0.706          pass              0.550             26.3                           0.335                5.53              0.815                                 ok           False                  False
   PEP          100.00                6            1.13              1.15        145.63                20.43         0.642          pass              0.571             35.7                           0.604                2.81              0.394                                 ok           False                  False
   CSX           80.00                5            1.46              0.48         46.69                20.12         0.608          pass              0.094             11.0                           0.231                0.16              0.181                                 ok           False                  False
   WMT           78.95               19            1.13              0.96        120.62                34.81         0.585          pass              0.165             15.4                           0.195                5.84              0.489                                 ok           False                  False
  CRWD           88.10               42            0.14              0.66        679.21                64.72         0.582          pass              0.741             89.1                           0.393               -9.24             -0.452 downtrend_blocked_slope_and_streak           False                  False
   ADP           95.83               24            0.57              0.89        221.62                31.58         0.580          pass              0.732             60.3                           0.356               -3.80             -0.290            downtrend_blocked_slope           False                  False
  UPRO           93.94               33            0.46              0.46        143.94                48.01         0.579          pass              0.739             52.1                           0.277               -4.90             -0.491                                 ok           False                  False
   EXC           76.92               13            0.70              0.23         46.49                19.22         0.570          pass              0.173             32.0                           0.399                3.78              0.415                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-06-17T11:00:05.904410-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:55:04.940733-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:50:01.959639-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:45:01.979292-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:40:01.956283-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:35:06.928976-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:30:05.890992-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:25:01.204897-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:20:02.964904-04:00 early_entry_1020 early_entry_shadow {"current_drop_pct": 0.53, "early_entry_score": 0.794, "early_reclaim_pct": 66.4, "entry_mode": "early", "error": "IDXX: no call expiries found in the 21-40 trading-day window.", "matched_signals": 45, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.602, "shadow_only": true, "success_rate": 93.33, "ticker": "IDXX", "timing_score": 0.392, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.794, "early_reclaim_pct": 66.4, "matched_signals": 45, "recovery_stability_score": 0.602, "success_rate": 93.33, "ticker": "IDXX", "timing_score": 0.392, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-17T10:15:03.936200-04:00 early_entry_1015 early_entry_shadow   {"current_drop_pct": 0.5, "early_entry_score": 0.751, "early_reclaim_pct": 71.6, "entry_mode": "early", "error": "CPRT: no call expiries found in the 21-40 trading-day window.", "matched_signals": 37, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.622, "shadow_only": true, "success_rate": 91.89, "ticker": "CPRT", "timing_score": 0.394, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.751, "early_reclaim_pct": 71.6, "matched_signals": 37, "recovery_stability_score": 0.622, "success_rate": 91.89, "ticker": "CPRT", "timing_score": 0.394, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260617110005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260617110005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260617110005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260617110005)

</details>
