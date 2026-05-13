# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 11:00:06 EDT`
Last processed slot: `manage_1100`

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
- Equity: `$33,663.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$60.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260618C00490000       2026-05-13                   0      3     13410.0                 13470.0         44.7           44.9      510.62         505.1            60.0                   0.45         97.14               35               0.5         52.16           57.83                  43.23                 154.0           10.0               0.12                      ok
```

## Today's Closed Trades (2026-05-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           80.95               21            4.06              2.41         83.97               115.69         0.596          pass              0.243             28.1                           0.252               15.69              1.363                                 ok            True                  False
  SNPS           96.30               27            1.58              5.68        510.78                43.23         0.545          pass              0.593              8.4                           0.126                4.96              0.664                                 ok            True                  False
  MDLZ           85.00               20            0.95              0.41         61.52                23.07         0.527          pass              0.344             30.4                           0.204                0.12              0.027                                 ok            True                  False
  REGN           90.91               22            1.53              7.74        720.09                32.61         0.516          pass              0.459             12.2                           0.099                3.79              0.319                                 ok            True                  False
  FAST           96.43               28            0.61              0.19         43.24                22.09         0.514          pass              0.623             17.2                           0.133               -1.50             -0.329                                 ok            True                  False
  CDNS           97.30               37            0.61              1.54        357.38                38.69         0.512          pass              0.849             72.6                           0.359                7.85              0.900                                 ok            True                  False
    ZS           82.05               39            0.81              0.83        145.82                59.81         0.505          pass              0.486             62.4                           0.379                7.62              1.106                                 ok            True                  False
  CHTR           76.47               17            2.54              2.63        146.79               118.13         0.782          pass              0.223             32.7                           0.582               -9.13             -1.353            downtrend_blocked_slope           False                  False
  GEHC           58.33               24            1.48              0.64         62.01                57.10         0.574          pass              0.235             28.1                           0.253                3.17              0.334                                 ok           False                  False
  ORLY           77.78                9            2.07              1.33         91.27                35.45         0.561          pass              0.111             18.5                           0.235               -1.91             -0.553 downtrend_blocked_slope_and_streak           False                  False
  SHOP           76.47               17            3.16              2.20         98.90                84.62         0.553          pass              0.176             24.8                           0.199              -20.26             -2.558 downtrend_blocked_slope_and_streak           False                  False
  MSFT           81.82               22            1.13              3.23        406.38                32.80         0.530          pass              0.276             31.5                           0.440               -5.02             -0.219           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-05-13T11:00:06.549783-04:00 early_entry_1100 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-13T10:55:05.050603-04:00 early_entry_1055 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-13T10:50:03.713971-04:00 early_entry_1050 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-13T10:45:06.364119-04:00 early_entry_1045 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-13T10:40:01.859562-04:00 early_entry_1040 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-13T10:35:05.886514-04:00 early_entry_1035 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-13T10:30:03.887456-04:00 early_entry_1030 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-13T10:25:06.096694-04:00 early_entry_1025         entry {"allocated_cash": 13410.0, "asset_type": "option", "contract_symbol": "SNPS260618C00490000", "contracts": 3, "early_entry_score": 0.822, "entry_mode": "early", "entry_option_price": 44.7, "execution_mode": "option", "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 154.0, "option_spread_pct": 12.08, "option_volume": 10.0, "success_rate": 97.14, "ticker": "SNPS", "timing_score": 0.556}
2026-05-13T10:20:06.278508-04:00 early_entry_1020 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate"}
2026-05-13T10:15:05.895485-04:00 early_entry_1015 entry_skipped                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_trade_after_option_and_timing_filters"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513110006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513110006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513110006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513110006)

</details>
