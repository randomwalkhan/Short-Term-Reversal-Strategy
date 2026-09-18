# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-18 10:00:06 EDT`
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

- Cash: `$32,735.80`
- Equity: `$68,740.30`
- Realized PnL: `$55,311.30`
- Unrealized PnL: `$3,429.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   WMT     option         option WMT261023C00108000       2026-09-17                   1    127     32575.5                 36004.5         2.57           2.84      106.54        107.65          bid_ask_mid                       2.84                bid_ask_mid                    True          3429.0                  10.53         83.33               24              0.89         24.93           24.48                  39.87                 249.0           74.0               0.12                      ok
```

## Today's Closed Trades (2026-09-18)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           96.88               32            1.61              2.22        196.52                82.85         0.621          pass              0.685             25.5                           0.235                9.28              1.837                                 ok            True                  False
  CTSH          100.00               17            2.25              0.97         61.46                39.55         0.528          pass              0.529              9.7                           0.119               -6.42             -0.002                                 ok            True                  False
  FTNT           85.00               20            2.40              2.91        171.33                57.60         0.513          pass              0.292             13.4                           0.197                7.72              1.165                                 ok            True                  False
  CRWD           77.78               18            3.14              5.39        243.39                97.92         0.638          pass              0.134              5.7                           0.169               10.71              1.749                                 ok           False                  False
  PYPL           94.12               34            0.49              0.18         52.86                57.74         0.616          pass              0.785             62.3                           0.656               -7.06             -0.425            downtrend_blocked_slope           False                  False
   EXC          100.00                7            1.09              0.33         42.50                15.46         0.565          pass              0.505             16.3                           0.113               -4.39             -0.461 downtrend_blocked_slope_and_streak           False                  False
   TRI           90.91               11            3.11              2.16         98.55                55.72         0.564          pass              0.373              6.4                           0.164              -13.75             -0.630 downtrend_blocked_slope_and_streak           False                  False
  ADSK           84.38               32            0.81              1.24        218.11                55.63         0.559          pass              0.379             19.8                           0.238               -8.69             -0.060           downtrend_blocked_streak           False                  False
   PEP          100.00                1            1.84              1.72        132.92                12.51         0.546          pass              0.551             32.2                           0.311               -5.30             -0.454 downtrend_blocked_slope_and_streak           False                  False
   ADP           94.74               19            0.82              1.56        271.57                22.18         0.537          pass              0.649             47.5                           0.322               -4.16             -0.046           downtrend_blocked_streak           False                  False
  ADBE           96.15               26            1.55              2.75        251.49                46.08         0.533          pass              0.624             21.3                           0.185              -12.95             -0.817 downtrend_blocked_slope_and_streak           False                  False
  PANW           53.85               13            3.68              9.67        370.92                79.31         0.529          pass              0.104             10.5                           0.160                8.83              1.406                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-09-18T10:00:06.717363-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T00:00:09.864377-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 92, 'empty': 1}
2026-09-17T15:10:01.182099-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-17T15:05:01.143983-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-17T15:00:04.868136-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-17T14:55:01.186160-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-17T14:50:04.102358-04:00       entry_1500              entry {"allocated_cash": 32575.5, "asset_type": "option", "contract_symbol": "WMT261023C00108000", "contracts": 127, "early_entry_score": 0.327, "entry_mode": "regular", "entry_option_price": 2.565, "execution_mode": "option", "matched_signals": 24, "option_liquidity_status": "ok", "option_open_interest": 249.0, "option_spread_pct": 12.09, "option_volume": 74.0, "success_rate": 83.33, "ticker": "WMT", "timing_score": 0.572}
2026-09-17T14:50:04.102358-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-17", "training_samples": 5767, "window": 5}
2026-09-17T12:00:02.509358-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:55:04.328741-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260918100006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260918100006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260918100006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260918100006)

</details>
