# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-06 09:45:03 EST`
Last processed slot: `manual`

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
- Equity: `$119,281.55`
- Realized PnL: `$119,631.55`
- Unrealized PnL: `$-10,350.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ORLY     option         option ORLY261218C00095000       2026-11-05                   1    345     64687.5                 54337.5         1.88           1.58       90.92         89.81          bid_ask_mid                       1.58                bid_ask_mid                    True        -10350.0                  -16.0         100.0               14              1.54         28.75           31.79                   25.4                2285.0          162.0               0.13                      ok
```

## Today's Closed Trades (2026-11-06)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  IDXX           96.88               32            0.97              4.54        668.77                77.01         0.653          pass              0.818             68.7                           0.646               18.53              2.422                      ok            True                   True
  AAPL          100.00               12            1.32              3.19        342.80                25.86         0.548          pass              0.547             26.3                           0.269               -2.33             -0.178                      ok            True                  False
  ISRG           89.47               19            1.72              5.66        466.10                42.48         0.527          pass              0.472             35.5                           0.557                1.80              0.389                      ok            True                  False
  INSM           81.40               43            0.61              0.46        108.56                61.78         0.527          pass              0.455             55.1                           0.408               15.75              1.738                      ok            True                  False
  MSFT          100.00               23            1.03              3.87        534.27                35.82         0.526          pass              0.735             65.3                           0.609                1.12              0.121                      ok            True                  False
  ORLY          100.00               11            1.80              1.16         90.99                25.42         0.522          pass              0.583             41.3                           0.445               -0.09              0.107                      ok            True                  False
  SBUX           81.82               11            1.87              1.39        105.57                31.38         0.501          pass              0.234             43.0                           0.442                3.35              0.459                      ok            True                  False
  ALNY           84.78               46            0.41              0.44        156.47               108.53         0.701          pass              0.617             73.1                           0.545              -30.36             -4.704 downtrend_blocked_slope           False                  False
  COST          100.00                2            1.98             14.76       1059.26                23.23         0.583          pass              0.493             11.7                           0.225                4.26              0.667                      ok           False                  False
  TMUS           69.23               13            1.77              1.99        159.74                69.87         0.572          pass              0.223             48.6                           0.572                7.65              1.031                      ok           False                  False
  MDLZ          100.00                1            2.56              1.20         66.31                30.66         0.562          pass              0.535             26.3                           0.361                2.05              0.667                      ok           False                  False
   KDP           80.00                5            2.17              0.56         36.65                35.93         0.559          pass              0.153             32.2                           0.383                4.07              0.549                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-11-06T00:00:05.873156-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                 {'saved': 91, 'empty': 2}
2026-11-05T15:10:05.513182-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-05T15:05:05.534747-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-05T15:00:06.437749-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-05T14:55:05.870253-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-05T14:50:06.583825-05:00       entry_1500              entry {"allocated_cash": 64687.5, "asset_type": "option", "contract_symbol": "ORLY261218C00095000", "contracts": 345, "early_entry_score": 0.515, "entry_mode": "regular", "entry_option_price": 1.875, "execution_mode": "option", "matched_signals": 14, "option_liquidity_status": "ok", "option_open_interest": 2285.0, "option_spread_pct": 13.33, "option_volume": 162.0, "success_rate": 100.0, "ticker": "ORLY", "timing_score": 0.528}
2026-11-05T14:50:06.583825-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                              {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-05", "training_samples": 6319, "window": 5}
2026-11-05T12:00:04.376215-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:55:05.652080-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:50:05.625919-05:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261106094503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261106094503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261106094503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261106094503)

</details>
