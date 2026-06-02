# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 10:45:01 EDT`
Last processed slot: `early_entry_1045`

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

- Cash: `$17,469.25`
- Equity: `$33,669.25`
- Realized PnL: `$23,669.25`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AMZN     option         option AMZN260717C00260000       2026-06-02                   0     15     16200.0                 16200.0         10.8           10.8      259.57        259.38          bid_ask_mid                       10.8                bid_ask_mid                    True             0.0                    0.0         90.62               32              0.65         30.52           30.52                  24.44                8913.0          913.0               0.02                      ok
```

## Today's Closed Trades (2026-06-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    MU           82.35               34            0.60              4.34       1032.88               101.73         0.731          pass              0.500             68.2                           0.298               50.91              4.614                                 ok            True                  False
  FTNT          100.00               11            2.13              2.20        146.20                71.69         0.687          pass              0.626             50.3                           0.558               13.83              1.230                                 ok            True                  False
  MNST           90.91               11            1.82              1.13         88.61                49.60         0.649          pass              0.385              7.4                           0.187               -1.20              0.157                                 ok            True                  False
  MELI           92.00               25            1.73             20.99       1721.99                60.28         0.599          pass              0.603             41.2                           0.559                7.26              0.725                                 ok            True                  False
  INTC           96.30               27            1.55              1.18        108.82                88.85         0.566          pass              0.772             67.2                           0.805               -0.49             -0.120                                 ok            True                  False
  AMGN           88.89               18            0.87              2.00        328.27                20.27         0.528          pass              0.518             58.3                           0.745                0.58              0.037                                 ok            True                  False
  CDNS           90.00               20            1.95              5.67        411.73                44.19         0.504          pass              0.499             38.3                           0.463               17.36              1.724                                 ok            True                  False
  INSM           50.00               12            3.65              2.71        104.87               110.78         0.692          pass              0.170             29.2                           0.497               -4.66             -0.307            downtrend_blocked_slope           False                  False
    ZS          100.00                2            8.78              9.57        151.61               157.27         0.581          pass              0.481              7.8                           0.157              -18.69             -2.807            downtrend_blocked_slope           False                  False
   WMT           76.92               13            1.35              1.08        114.14                32.65         0.575          pass              0.109             10.4                           0.210              -15.22             -1.709 downtrend_blocked_slope_and_streak           False                  False
  REGN           88.24               34            0.54              2.27        599.69                42.53         0.543          pass              0.627             64.5                           0.676               -4.98             -0.630 downtrend_blocked_slope_and_streak           False                  False
   HON           71.43                7            1.65              2.73        235.37                24.20         0.539          pass              0.069              4.9                           0.080                7.09              0.956                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-06-02T10:45:01.434257-04:00 early_entry_1045                   entry {"allocated_cash": 16200.0, "asset_type": "option", "contract_symbol": "AMZN260717C00260000", "contracts": 15, "early_entry_score": 0.702, "entry_mode": "early", "entry_option_price": 10.8, "execution_mode": "option", "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 8913.0, "option_spread_pct": 1.85, "option_volume": 913.0, "success_rate": 90.62, "ticker": "AMZN", "timing_score": 0.457}
2026-06-02T10:40:04.457109-04:00 early_entry_1040           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-06-02T10:35:04.553797-04:00 early_entry_1035           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-06-02T10:30:04.405006-04:00 early_entry_1030           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-06-02T10:25:01.235572-04:00 early_entry_1025           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-06-02T10:20:01.327977-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-06-02T10:15:02.269482-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_trade_after_option_and_timing_filters"}
2026-06-02T10:15:02.269482-04:00 early_entry_1015 entry_candidate_skipped                                                                                                                                                                               {"early_entry_score": 0.679, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 117.0, "option_spread_pct": 24.24, "option_volume": 5.0, "reason": "no_trade_low_option_liquidity", "ticker": "CHTR", "timing_score": 0.442}
2026-06-02T10:10:06.260122-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-06-02T10:05:01.451088-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602104501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602104501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602104501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602104501)

</details>
