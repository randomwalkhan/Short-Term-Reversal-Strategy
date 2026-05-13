# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 11:50:06 EDT`
Last processed slot: `manage_1200`

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
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$20,193.50`
- Equity: `$33,273.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$-330.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260618C00490000       2026-05-13                   0      3     13410.0                 13080.0         44.7           43.6      510.62         505.2          -330.0                  -2.46         97.14               35               0.5         52.16           56.22                  43.23                 154.0           10.0               0.12                      ok
```

## Today's Closed Trades (2026-05-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           85.71               14            4.72              2.81         83.80               115.69         0.607          pass              0.289             16.5                           0.175               14.90              1.332                                 ok            True                  False
  MDLZ           85.71               14            1.30              0.56         61.46                23.07         0.547          pass              0.251              5.8                           0.213               -0.24              0.011                                 ok            True                  False
  SNPS           96.30               27            1.56              5.61        510.81                43.23         0.544          pass              0.622             18.2                           0.361                4.98              0.665                                 ok            True                  False
  CDNS           97.06               34            0.98              2.45        356.99                38.69         0.511          pass              0.780             56.4                           0.373                7.45              0.883                                 ok            True                  False
  CHTR           73.33               15            2.94              3.04        146.62               118.13         0.770          pass              0.176             22.0                           0.297               -9.50             -1.372            downtrend_blocked_slope           False                  False
 CMCSA           92.31               13            1.10              0.19         24.82                62.10         0.726          pass              0.498             25.7                           0.202               -7.98             -1.027 downtrend_blocked_slope_and_streak           False                  False
  INTC          100.00               42            0.04              0.03        120.60               109.00         0.654          pass              0.962             98.9                           0.466               27.25              3.192                                 ok           False                  False
  GEHC           73.68               38            0.65              0.28         62.17                57.10         0.560          pass              0.448             68.4                           0.780                4.03              0.372                                 ok           False                  False
  SHOP           80.00               20            2.87              2.01         98.98                84.62         0.556          pass              0.217             31.5                           0.529              -20.03             -2.545 downtrend_blocked_slope_and_streak           False                  False
   ADP          100.00                9            2.63              3.93        212.12                33.54         0.539          pass              0.556             34.0                           0.254               -3.19             -0.119                                 ok           False                  False
  MELI           80.00               15            2.37             26.18       1567.56                57.67         0.537          pass              0.253             55.4                           0.810              -12.77             -1.718            downtrend_blocked_slope           False                  False
   PEP           90.91               11            1.51              1.61        151.16                21.96         0.533          pass              0.382             10.5                           0.277               -3.70             -0.461            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-13T11:50:06.013562-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T11:45:03.915734-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T11:23:31.678775-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T11:05:05.896760-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T11:00:06.549783-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T10:55:05.050603-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T10:50:03.713971-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T10:45:06.364119-04:00 early_entry_1045 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T10:40:01.859562-04:00 early_entry_1040 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T10:35:05.886514-04:00 early_entry_1035 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513115006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513115006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513115006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513115006)

</details>
