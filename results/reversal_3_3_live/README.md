# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-10 11:15:04 EDT`
Last processed slot: `early_entry_1115`

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

- Cash: `$15,257.25`
- Equity: `$30,222.25`
- Realized PnL: `$20,222.25`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH260717C00055000       2026-06-09                   1     73     14965.0                 14965.0         2.05           2.05       52.68         52.48          bid_ask_mid                       2.05                bid_ask_mid                    True             0.0                    0.0         93.55               31              0.59         45.34           47.78                  51.28                1420.0           78.0                0.1                      ok
```

## Today's Closed Trades (2026-06-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  CSCO           96.15               26            1.00              0.84        120.00                60.79         0.629          pass              0.690             40.0                           0.231               -0.43              0.135                  ok            True                  False
  MRVL          100.00               14            3.97              7.41        263.70               141.19         0.623          pass              0.560             23.7                           0.147               28.98              3.464                  ok            True                  False
  TEAM           91.89               37            1.00              0.67         95.32                85.52         0.599          pass              0.790             77.7                           0.615                6.27             -0.237                  ok            True                   True
  WDAY           89.19               37            0.78              0.76        139.90                67.85         0.572          pass              0.730             82.5                           0.677               11.76              0.573                  ok            True                   True
  CTSH           90.32               31            0.75              0.28         52.82                47.83         0.558          pass              0.678             69.1                           0.489               -1.16             -0.413                  ok            True                  False
  REGN           84.85               33            0.86              3.72        614.59                44.80         0.537          pass              0.461             41.4                           0.338               -2.69             -0.030                  ok            True                  False
  CDNS           92.31               26            1.29              3.52        389.39                58.96         0.535          pass              0.687             66.3                           0.313                3.16              0.255                  ok            True                  False
   CSX           91.30               23            0.69              0.23         47.18                21.23         0.531          pass              0.586             48.4                           0.283               -0.09              0.277                  ok            True                  False
  ISRG           82.35               17            1.74              5.21        424.38                33.80         0.526          pass              0.215             17.8                           0.194                0.15              0.073                  ok            True                  False
  ADBE           83.33               36            0.84              1.39        237.28                49.90         0.509          pass              0.517             68.0                           0.636               -0.99             -0.422                  ok            True                  False
  DXCM           80.00               15            2.39              1.31         77.63                47.05         0.509          pass              0.131             15.6                           0.113                8.63              0.703                  ok            True                  False
  VRTX           96.15               26            1.06              3.30        444.35                26.58         0.508          pass              0.648             30.3                           0.177                0.88              0.063                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-06-10T11:15:04.333810-04:00 early_entry_1115 early_entry_shadow {"contract_symbol": "TEAM260717C00095000", "current_drop_pct": 1.0, "early_entry_score": 0.79, "early_reclaim_pct": 77.7, "entry_ask": 9.7, "entry_bid": 8.2, "entry_mode": "early", "entry_option_price": 8.95, "hypothetical_budget": 7628.63, "hypothetical_contracts": 8, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 16.76, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.615, "shadow_only": true, "success_rate": 91.89, "ticker": "TEAM", "timing_score": 0.599, "top_candidates": [{"current_drop_pct": 1.0, "early_entry_score": 0.79, "early_reclaim_pct": 77.7, "matched_signals": 37, "recovery_stability_score": 0.615, "success_rate": 91.89, "ticker": "TEAM", "timing_score": 0.599, "trend_health_status": "ok"}, {"current_drop_pct": 0.78, "early_entry_score": 0.73, "early_reclaim_pct": 82.5, "matched_signals": 37, "recovery_stability_score": 0.677, "success_rate": 89.19, "ticker": "WDAY", "timing_score": 0.572, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-10T11:10:04.307912-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T11:05:01.212784-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T11:00:04.519159-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T10:55:01.275812-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T10:50:04.358355-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                  {"contract_symbol": "ABNB260717C00135000", "current_drop_pct": 0.54, "early_entry_score": 0.769, "early_reclaim_pct": 76.2, "entry_ask": 4.45, "entry_bid": 4.2, "entry_mode": "early", "entry_option_price": 4.325, "hypothetical_budget": 7628.63, "hypothetical_contracts": 17, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 490.0, "option_spread_pct": 5.78, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.608, "shadow_only": true, "success_rate": 91.89, "ticker": "ABNB", "timing_score": 0.431, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.769, "early_reclaim_pct": 76.2, "matched_signals": 37, "recovery_stability_score": 0.608, "success_rate": 91.89, "ticker": "ABNB", "timing_score": 0.431, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-10T10:45:02.614919-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T10:40:02.425306-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                    {"contract_symbol": "WDAY260717C00140000", "current_drop_pct": 0.61, "early_entry_score": 0.782, "early_reclaim_pct": 86.4, "entry_ask": 11.0, "entry_bid": 10.1, "entry_mode": "early", "entry_option_price": 10.55, "hypothetical_budget": 7628.63, "hypothetical_contracts": 7, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 684.0, "option_spread_pct": 8.53, "option_volume": 78.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.625, "shadow_only": true, "success_rate": 90.0, "ticker": "WDAY", "timing_score": 0.564, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.782, "early_reclaim_pct": 86.4, "matched_signals": 40, "recovery_stability_score": 0.625, "success_rate": 90.0, "ticker": "WDAY", "timing_score": 0.564, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-10T10:35:05.364684-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T10:30:02.359005-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260610111504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260610111504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260610111504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260610111504)

</details>
