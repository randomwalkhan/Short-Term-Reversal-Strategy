# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-15 09:55:04 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$38,116.10`
- Equity: `$74,116.10`
- Realized PnL: `$66,116.10`
- Unrealized PnL: `$-2,000.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   EXC     option         option EXC261016C00043000       2026-09-14                   1    400     38000.0                 36000.0         0.95            0.9       42.87         42.43          bid_ask_mid                        0.9                bid_ask_mid                    True         -2000.0                  -5.26         100.0               11              0.67         20.46           27.17                  14.68                 123.0           93.0               0.11                      ok
```

## Today's Closed Trades (2026-09-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           96.88               32            1.54              2.07        190.84                82.09         0.610          pass              0.716             36.3                           0.397                0.21             -0.033                                 ok            True                  False
  PANW           80.49               41            0.80              2.09        373.05                81.04         0.593          pass              0.448             58.5                           0.499               -2.92              0.041                                 ok            True                  False
  TEAM          100.00               31            1.50              2.02        191.90                63.46         0.566          pass              0.746             49.8                           0.485               -2.21             -0.298                                 ok            True                  False
   ADP           96.00               25            0.52              1.00        276.20                26.20         0.532          pass              0.761             69.1                           0.669               -3.21             -0.474                                 ok            True                  False
  FTNT           90.00               40            0.73              0.88        169.80                60.22         0.530          pass              0.759             79.8                           0.612               -1.17              0.190                                 ok            True                   True
  ALNY           84.21               19            2.25              3.94        248.30                49.37         0.506          pass              0.294             23.7                           0.227                1.52             -0.221                                 ok            True                  False
  AMGN           92.86               14            1.27              3.38        380.05                45.29         0.622          pass              0.477             15.3                           0.197              -12.38             -1.913 downtrend_blocked_slope_and_streak           False                  False
  PYPL           92.68               41            0.09              0.04         54.01                58.07         0.603          pass              0.870             90.4                           0.453                2.75              0.044                                 ok           False                  False
  MSTR           77.78               18            4.62              4.43        135.04               103.17         0.581          pass              0.153             13.8                           0.163               -1.75              0.139           downtrend_blocked_streak           False                  False
   WMT           85.71               35            0.34              0.26        108.97                40.03         0.564          pass              0.549             57.9                           0.511                3.66              0.241                                 ok           False                  False
   PEP          100.00                9            0.94              0.89        135.96                16.22         0.564          pass              0.516             19.8                           0.187               -2.73             -0.263            downtrend_blocked_slope           False                  False
   KHC           90.00               10            1.17              0.20         24.20                26.10         0.563          pass              0.465             47.2                           0.442               -5.10             -0.546            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-09-15T00:00:03.212916-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 93}
2026-09-14T15:10:01.099454-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-14T15:05:01.081991-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-14T15:00:05.039225-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-14T14:55:02.132179-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-14T14:50:04.030674-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"allocated_cash": 38000.0, "asset_type": "option", "contract_symbol": "EXC261016C00043000", "contracts": 400, "early_entry_score": 0.606, "entry_mode": "regular", "entry_option_price": 0.95, "execution_mode": "option", "matched_signals": 11, "option_liquidity_status": "ok", "option_open_interest": 123.0, "option_spread_pct": 10.53, "option_volume": 93.0, "success_rate": 100.0, "ticker": "EXC", "timing_score": 0.551}
2026-09-14T14:50:04.030674-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-14", "training_samples": 5764, "window": 5}
2026-09-14T12:00:04.262790-04:00 early_entry_1200 early_entry_shadow   {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.73, "early_entry_score": 0.804, "early_reclaim_pct": 69.6, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.663, "shadow_only": true, "success_rate": 96.97, "ticker": "PCAR", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.804, "early_reclaim_pct": 69.6, "matched_signals": 33, "recovery_stability_score": 0.663, "success_rate": 96.97, "ticker": "PCAR", "timing_score": 0.42, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T11:55:01.111232-04:00 early_entry_1155 early_entry_shadow     {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.8, "early_entry_score": 0.783, "early_reclaim_pct": 66.7, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.61, "shadow_only": true, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.428, "top_candidates": [{"current_drop_pct": 0.8, "early_entry_score": 0.783, "early_reclaim_pct": 66.7, "matched_signals": 31, "recovery_stability_score": 0.61, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.428, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T11:50:01.134863-04:00 early_entry_1150 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.85, "early_entry_score": 0.777, "early_reclaim_pct": 64.9, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.577, "shadow_only": true, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.425, "top_candidates": [{"current_drop_pct": 0.85, "early_entry_score": 0.777, "early_reclaim_pct": 64.9, "matched_signals": 31, "recovery_stability_score": 0.577, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.425, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260915095504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260915095504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260915095504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260915095504)

</details>
