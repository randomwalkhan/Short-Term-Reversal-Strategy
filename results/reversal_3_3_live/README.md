# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-05 15:30:06 EST`
Last processed slot: `manage_1530`

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

- Cash: `$64,944.05`
- Equity: `$124,456.55`
- Realized PnL: `$119,631.55`
- Unrealized PnL: `$-5,175.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ORLY     option         option ORLY261218C00095000       2026-11-05                   0    345     64687.5                 59512.5         1.88           1.72       90.92         90.86          bid_ask_mid                       1.72                bid_ask_mid                    True         -5175.0                   -8.0         100.0               14              1.54         28.75           28.16                   25.4                2285.0          162.0               0.13                      ok
```

## Today's Closed Trades (2026-11-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MDLZ           93.75               16            0.62              0.29         67.25                30.79         0.595          pass              0.528             20.8                           0.250                2.72              0.570                      ok            True                  False
  AAPL          100.00               14            1.25              3.07        348.20                25.40         0.529          pass              0.603             41.2                           0.352               -0.89             -0.163                      ok            True                  False
  ORLY          100.00               13            1.60              1.04         91.90                25.40         0.527          pass              0.540             22.5                           0.382               -1.24              0.002                      ok            True                  False
   WMT           84.21               19            0.86              0.78        128.84                26.34         0.526          pass              0.251              8.6                           0.176                5.73              0.785                      ok            True                  False
  FAST           92.86               14            1.03              0.39         53.04                21.86         0.515          pass              0.446              8.3                           0.213                0.37              0.184                      ok            True                  False
   KHC           90.00               30            0.75              0.13         25.38                36.26         0.506          pass              0.613             54.2                           0.334                0.64              0.181                      ok            True                  False
   XEL           81.25               16            0.96              0.54         80.27                19.85         0.500          pass              0.291             56.0                           0.362                1.05              0.249                      ok            True                  False
  ALNY           84.21               38            0.82              0.92        160.68               108.65         0.699          pass              0.493             41.3                           0.396              -29.71             -4.734 downtrend_blocked_slope           False                  False
 GOOGL           77.78                9            2.00              4.04        287.20                52.55         0.597          pass              0.214             51.3                           0.355              -12.66             -1.714 downtrend_blocked_slope           False                  False
  GOOG           83.33               12            1.75              3.52        285.79                51.02         0.591          pass              0.325             54.7                           0.369              -12.00             -1.643 downtrend_blocked_slope           False                  False
  REGN           75.00                4            2.79             18.19        922.87                52.52         0.562          pass              0.063              2.4                           0.119               10.45              1.906                      ok           False                  False
 CMCSA           92.86               28            0.14              0.02         24.84                35.54         0.561          pass              0.787             89.4                           0.666                8.65              1.130                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-11-05T15:10:05.513182-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-05T15:05:05.534747-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-05T15:00:06.437749-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-05T14:55:05.870253-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-05T14:50:06.583825-05:00       entry_1500              entry {"allocated_cash": 64687.5, "asset_type": "option", "contract_symbol": "ORLY261218C00095000", "contracts": 345, "early_entry_score": 0.515, "entry_mode": "regular", "entry_option_price": 1.875, "execution_mode": "option", "matched_signals": 14, "option_liquidity_status": "ok", "option_open_interest": 2285.0, "option_spread_pct": 13.33, "option_volume": 162.0, "success_rate": 100.0, "ticker": "ORLY", "timing_score": 0.528}
2026-11-05T14:50:06.583825-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                              {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-05", "training_samples": 6319, "window": 5}
2026-11-05T12:00:04.376215-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:55:05.652080-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:50:05.625919-05:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:45:05.647675-05:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261105153006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261105153006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261105153006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261105153006)

</details>
