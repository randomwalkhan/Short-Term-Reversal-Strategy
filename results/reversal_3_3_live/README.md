# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-01 10:35:04 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$47,718.10`
- Equity: `$47,718.10`
- Realized PnL: `$37,718.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SHOP     option         option SHOP261016C00150000     30          2026-08-31         2026-09-01          8.2        7.38 -2460.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  TEAM           88.57               35            1.41              1.92        193.35               115.35         0.751          pass              0.647             58.9                           0.633               17.44              1.482                      ok            True                  False
  SHOP           91.67               24            2.15              2.22        146.42                69.51         0.598          pass              0.601             45.5                           0.777               -2.99              0.088                      ok            True                  False
  CSCO           83.33               30            1.15              0.89        110.11                40.87         0.540          pass              0.332             18.6                           0.257               -3.26             -0.102                      ok            True                  False
  NVDA           86.21               29            1.15              1.78        219.74                45.52         0.528          pass              0.504             53.0                           0.656               -0.81              0.139                      ok            True                  False
   CSX           90.91               11            1.49              0.53         50.28                15.01         0.519          pass              0.386             12.0                           0.142               -1.63              0.017                      ok            True                  False
  DRAM           83.87               31            2.36              0.94         56.50                66.99         0.519          pass              0.352             19.0                           0.274                0.83              0.075                      ok            True                  False
  CPRT           85.71               35            0.73              0.17         32.92                40.13         0.508          pass              0.566             65.2                           0.782                3.31              0.123                      ok            True                  False
  CHTR           89.47               19            2.95              3.14        151.09                52.85         0.502          pass              0.451             29.3                           0.358                2.67              0.247                      ok            True                  False
  MNST           94.12               34            0.38              0.12         45.87               551.67         1.000          pass              0.708             23.9                           0.271                0.49             -0.104                      ok           False                  False
  INSM           87.18               39            0.62              0.53        121.59               109.80         0.786          pass              0.640             58.8                           0.494               -5.65             -0.682 downtrend_blocked_slope           False                  False
   WDC           77.78               36            0.30              0.94        450.15                84.65         0.669          pass              0.508             89.1                           0.712              -16.19             -1.172 downtrend_blocked_slope           False                  False
   STX           83.87               31            1.38              8.02        824.94                71.45         0.585          pass              0.471             56.4                           0.583              -17.88             -1.203 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-09-01T10:35:04.145370-04:00 early_entry_1035 early_entry_shadow                                              {"contract_symbol": "INTU261016C00330000", "current_drop_pct": 0.83, "early_entry_score": 0.726, "early_reclaim_pct": 73.2, "entry_ask": 35.9, "entry_bid": 31.6, "entry_mode": "early", "entry_option_price": 33.75, "hypothetical_budget": 23859.05, "hypothetical_contracts": 7, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 179.0, "option_spread_pct": 12.74, "option_volume": 32.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.853, "shadow_only": true, "success_rate": 91.18, "ticker": "INTU", "timing_score": 0.485, "top_candidates": [{"current_drop_pct": 0.83, "early_entry_score": 0.726, "early_reclaim_pct": 73.2, "matched_signals": 34, "recovery_stability_score": 0.853, "success_rate": 91.18, "ticker": "INTU", "timing_score": 0.485, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-01T10:30:06.594545-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T10:25:01.815203-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T10:20:03.001967-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T10:15:02.023349-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T10:10:02.052599-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T10:05:04.005187-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "ABNB261002C00182500", "current_drop_pct": 0.51, "early_entry_score": 0.792, "early_reclaim_pct": 71.0, "entry_ask": 7.85, "entry_bid": 5.35, "entry_mode": "early", "entry_option_price": 6.6, "hypothetical_budget": 23859.05, "hypothetical_contracts": 36, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 37.88, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.606, "shadow_only": true, "success_rate": 93.75, "ticker": "ABNB", "timing_score": 0.658, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.792, "early_reclaim_pct": 71.0, "matched_signals": 32, "recovery_stability_score": 0.606, "success_rate": 93.75, "ticker": "ABNB", "timing_score": 0.658, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-01T10:00:06.717269-04:00 early_entry_1000 early_entry_shadow                  {"contract_symbol": "DASH261016C00230000", "current_drop_pct": 0.81, "early_entry_score": 0.801, "early_reclaim_pct": 62.4, "entry_ask": 14.4, "entry_bid": 11.0, "entry_mode": "early", "entry_option_price": 12.7, "hypothetical_budget": 23859.05, "hypothetical_contracts": 18, "matched_signals": 36, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 358.0, "option_spread_pct": 26.77, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.67, "shadow_only": true, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.401, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.801, "early_reclaim_pct": 62.4, "matched_signals": 36, "recovery_stability_score": 0.67, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.401, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-01T09:50:02.006317-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"asset_type": "option", "contract_symbol": "SHOP261016C00150000", "fill_price": 7.38, "pnl": -2460.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SHOP"}
2026-09-01T00:00:06.642760-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260901103504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260901103504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260901103504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260901103504)

</details>
