# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 10:15:06 EDT`
Last processed slot: `early_entry_1015`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$18,731.75`
- Equity: `$36,331.75`
- Realized PnL: `$26,331.75`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   TXN     option         option TXN260717C00310000       2026-06-03                   0      8     17600.0                 17600.0         22.0           22.0      306.54        306.54          bid_ask_mid                       22.0                bid_ask_mid                    True             0.0                    0.0         100.0               30              0.51         54.92           54.92                   42.9                1851.0           30.0                0.1                      ok
```

## Today's Closed Trades (2026-06-03)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
    MU           81.82               33            0.62              4.63       1062.12               101.17         0.719          pass              0.496             74.2                           0.529               51.34              4.575                  ok            True                  False
  CSCO           95.65               23            1.10              0.99        127.58                53.71         0.615          pass              0.729             60.3                           0.643                9.72              0.905                  ok            True                  False
  MELI           94.12               34            1.04             12.15       1667.62                61.01         0.589          pass              0.732             45.4                           0.581                3.80              0.361                  ok            True                  False
  FTNT          100.00               38            0.78              0.81        148.51                71.83         0.573          pass              0.885             80.2                           0.842               15.72              1.530                  ok            True                   True
   TXN          100.00               30            0.51              1.11        307.64                42.90         0.547          pass              0.813             75.0                           0.619                1.40              0.007                  ok            True                   True
  MCHP           96.30               27            0.68              0.46         96.76                44.80         0.532          pass              0.800             77.8                           0.680                5.42              0.401                  ok            True                  False
   CEG           81.82               22            2.02              3.86        270.99                55.62         0.526          pass              0.207              8.8                           0.189                2.48             -0.288                  ok            True                  False
  CDNS           92.31               13            2.36              6.87        413.45                43.85         0.521          pass              0.506             35.2                           0.630               20.25              1.842                  ok            True                  False
  CRWD           82.35               17            1.96             10.53        764.44                51.19         0.519          pass              0.293             43.9                           0.634               22.21              2.210                  ok            True                  False
  WDAY           84.00               25            2.58              2.68        147.73                75.59         0.517          pass              0.361             34.3                           0.616               12.14              2.088                  ok            True                  False
   ADP          100.00               13            2.31              3.73        229.58                34.09         0.510          pass              0.510             13.1                           0.101                2.45              0.421                  ok            True                  False
 CMCSA           80.00               10            1.71              0.30         24.72                17.52         0.509          pass              0.071              6.6                           0.112               -1.51             -0.101                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-06-03T10:15:06.039702-04:00 early_entry_1015                   entry {"allocated_cash": 17600.0, "asset_type": "option", "contract_symbol": "TXN260717C00310000", "contracts": 8, "early_entry_score": 0.813, "entry_mode": "early", "entry_option_price": 22.0, "execution_mode": "option", "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 1851.0, "option_spread_pct": 10.0, "option_volume": 30.0, "success_rate": 100.0, "ticker": "TXN", "timing_score": 0.547}
2026-06-03T10:15:06.039702-04:00 early_entry_1015 entry_candidate_skipped                                                                                                                                                                          {"early_entry_score": 0.885, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 771.0, "option_spread_pct": 18.79, "option_volume": 13.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.573}
2026-06-03T10:10:05.039776-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_trade_after_option_and_timing_filters"}
2026-06-03T10:10:05.039776-04:00 early_entry_1010 entry_candidate_skipped                                                                                                                                                                           {"early_entry_score": 0.848, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 383.0, "option_spread_pct": 21.64, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.579}
2026-06-03T10:05:03.196018-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate"}
2026-06-03T10:00:06.995022-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate"}
2026-06-03T09:20:04.119925-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                    {'saved': 92}
2026-06-02T15:10:01.501174-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-06-02T15:05:06.421436-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-06-02T15:00:02.491254-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603101506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603101506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603101506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603101506)

</details>
