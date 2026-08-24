# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-24 09:40:01 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$57,703.00`
- Equity: `$57,703.00`
- Realized PnL: `$47,703.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-24)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ALNY           84.62               26            1.54              2.55        235.13               131.78         0.818          pass              0.343             10.3                           0.229                7.19              0.739                                 ok            True                  False
  ASML           85.71               28            1.41             17.37       1756.32                48.84         0.546          pass              0.430             34.3                           0.317                0.32             -0.268                                 ok            True                  False
  INSM           83.33               30            1.54              1.36        125.19               110.84         0.779          pass              0.343             14.2                           0.136               -8.10             -0.633 downtrend_blocked_slope_and_streak           False                  False
   APP           71.11               45            0.46              0.98        305.35                90.15         0.665          pass              0.434             55.8                           0.441              -10.22             -0.630            downtrend_blocked_slope           False                  False
  AMAT           89.47               19            3.28             11.32        487.47                82.60         0.624          pass              0.382              2.4                           0.350               -8.71             -1.039            downtrend_blocked_slope           False                  False
  MCHP           84.62               26            2.36              1.25         75.09                69.56         0.607          pass              0.300              3.3                           0.156               -9.28             -0.824            downtrend_blocked_slope           False                  False
  GEHC           97.56               41            0.19              0.10         74.78                48.71         0.581          pass              0.855             65.7                           0.410                2.38              0.282                                 ok           False                  False
  UPRO           79.31               29            0.86              0.90        149.52                39.04         0.567          pass              0.239             18.7                           0.267               -4.10             -0.484            downtrend_blocked_slope           False                  False
  DXCM           90.24               41            0.21              0.13         92.28                49.72         0.555          pass              0.759             76.7                           0.558                5.13              0.289                                 ok           False                  False
  AMGN          100.00               30            0.16              0.48        439.12                30.84         0.553          pass              0.834             81.9                           0.555                5.75              0.727                                 ok           False                  False
   AEP           95.00               20            0.50              0.43        120.76                19.55         0.546          pass              0.564             14.1                           0.261               -2.04             -0.131           downtrend_blocked_streak           False                  False
  CSCO           85.71               35            0.83              0.64        110.76                42.43         0.539          pass              0.488             38.3                           0.339              -10.16             -1.164            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-08-24T09:20:01.323688-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 93}
2026-08-21T12:00:13.505037-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-21T11:55:10.146119-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-21T11:50:07.256034-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-21T11:50:07.256034-04:00      manage_1200               exit                                                                                                                                                                                                                                              {"asset_type": "option", "contract_symbol": "ABNB261016C00180000", "fill_price": 14.125, "pnl": 4565.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 17.22, "ticker": "ABNB"}
2026-08-21T11:15:05.200635-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-21T10:36:48.615754-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-21T10:18:45.233650-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-21T00:00:05.323227-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 93}
2026-08-20T14:55:07.817083-04:00       entry_1500              entry {"allocated_cash": 26510.0, "asset_type": "option", "contract_symbol": "ABNB261016C00180000", "contracts": 22, "early_entry_score": 0.826, "entry_mode": "regular", "entry_option_price": 12.05, "execution_mode": "option", "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 783.0, "option_spread_pct": 5.81, "option_volume": 31.0, "success_rate": 93.94, "ticker": "ABNB", "timing_score": 0.625}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260824094001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260824094001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260824094001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260824094001)

</details>
