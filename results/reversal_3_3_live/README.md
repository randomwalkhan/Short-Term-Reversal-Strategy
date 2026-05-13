# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 10:40:01 EDT`
Last processed slot: `manage_1030`

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
- Equity: `$33,348.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$-255.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260618C00490000       2026-05-13                   0      3     13410.0                 13155.0         44.7          43.85      510.62        506.35          -255.0                   -1.9         97.14               35               0.5         52.16            55.5                  43.23                 154.0           10.0               0.12                      ok
```

## Today's Closed Trades (2026-05-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC          100.00               34            0.96              0.81        120.26               109.00         0.649            pass              0.842             72.4                           0.736               26.07              3.150                                 ok            True                   True
  TEAM           81.82               22            3.92              2.33         84.00               115.69         0.599            pass              0.280             30.6                           0.368               15.86              1.370                                 ok            True                  False
  SNPS           96.67               30            1.32              4.74        511.18                43.23         0.543            pass              0.624             12.2                           0.292                5.24              0.676                                 ok            True                  False
   ADP          100.00               10            2.45              3.67        212.24                33.54         0.542            pass              0.569             38.4                           0.328               -3.02             -0.111                                 ok            True                  False
    ZS           83.78               37            0.88              0.90        145.78                59.81         0.516            pass              0.510             59.1                           0.496                7.54              1.102                                 ok            True                  False
  MCHP           84.85               33            0.83              0.57         97.46                50.72         0.501            pass              0.520             62.5                           0.462                7.45              0.752                                 ok            True                  False
  MDLZ           84.62               26            0.75              0.32         61.56                23.07         0.500 below_threshold              0.415             45.2                           0.254                0.33              0.036                                 ok            True                  False
  CHTR           76.47               17            2.54              2.63        146.79               118.13         0.781            pass              0.222             32.5                           0.566               -9.13             -1.354            downtrend_blocked_slope           False                  False
  ORLY           87.50                8            2.12              1.37         91.25                35.45         0.583            pass              0.273              4.9                           0.076               -1.96             -0.556 downtrend_blocked_slope_and_streak           False                  False
  GEHC           58.33               24            1.53              0.66         62.01                57.10         0.572            pass              0.228             25.8                           0.222                3.12              0.332                                 ok           False                  False
  SHOP           80.00               20            2.87              2.01         98.98                84.62         0.556            pass              0.217             31.6                           0.366              -20.03             -2.545 downtrend_blocked_slope_and_streak           False                  False
  MSFT           84.21               19            1.39              3.96        406.07                32.80         0.538            pass              0.275             16.2                           0.239               -5.26             -0.230           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-05-13T10:40:01.859562-04:00 early_entry_1040           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-13T10:35:05.886514-04:00 early_entry_1035           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-13T10:30:03.887456-04:00 early_entry_1030           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-13T10:25:06.096694-04:00 early_entry_1025                   entry {"allocated_cash": 13410.0, "asset_type": "option", "contract_symbol": "SNPS260618C00490000", "contracts": 3, "early_entry_score": 0.822, "entry_mode": "early", "entry_option_price": 44.7, "execution_mode": "option", "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 154.0, "option_spread_pct": 12.08, "option_volume": 10.0, "success_rate": 97.14, "ticker": "SNPS", "timing_score": 0.556}
2026-05-13T10:20:06.278508-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate"}
2026-05-13T10:15:05.895485-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-13T10:15:05.895485-04:00 early_entry_1015 entry_candidate_skipped                                                                                                                                                            {"early_entry_score": 0.815, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 14.0, "option_spread_pct": 21.38, "option_volume": 8.0, "reason": "no_trade_low_option_liquidity", "ticker": "TTWO", "timing_score": 0.437}
2026-05-13T10:10:06.807841-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate"}
2026-05-13T10:05:05.859086-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate"}
2026-05-13T10:00:05.846029-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513104001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513104001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513104001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513104001)

</details>
