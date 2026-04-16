# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-16 14:40:06 EDT`
Last processed slot: `manage_1430`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while share-fallback positions also run take-profit and stop loss scans in after-hours / overnight / pre-market
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Fallback execution: buy shares when the option fails the liquidity gate; use `+3% / -3%` for common-stock fallback and `+5% / -5%` for leveraged-ETF shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; share positions can additionally trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$7,327.92`
- Equity: `$13,537.92`
- Realized PnL: `$4,347.92`
- Unrealized PnL: `$-810.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   HON     option         option HON260515C00240000       2026-04-15                   1     18      7020.0                  6210.0          3.9           3.45      231.34         229.2          -810.0                 -11.54         100.0               22              0.82         27.49           29.25                  23.78                2322.0          110.0               0.05                      ok
```

## Today's Closed Trades (2026-04-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               31            0.90              4.76        751.89                24.02            True
   HON          100.00               14            1.32              2.14        231.27                23.34            True
  MRVL           97.44               39            0.63              0.59        134.34                70.04            True
   WDC           96.97               33            2.05              5.24        362.75                79.90            True
   AEP           94.74               19            0.71              0.67        134.10                19.19            True
  ROST           90.91               11            1.55              2.44        223.11                24.88            True
  ALNY           90.00               10            2.97              6.94        330.42                43.40            True
  ISRG           90.00               10            2.61              8.57        464.69                23.09            True
  DXCM           88.64               44            0.53              0.23         61.44                31.33            True
  ORLY           87.50               32            0.83              0.55         93.37                23.50            True
  KLAC           86.21               29            1.41             17.30       1740.69                51.26            True
  TSLA           83.33               36            1.02              2.79        390.75                50.86            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-16T14:40:06.525547-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-16T14:35:06.445500-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-16T14:30:06.437775-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-16T14:25:06.447570-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-16T14:10:06.435946-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-16T14:05:06.594374-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-16T14:00:06.440718-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-16T13:55:06.472928-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-16T13:40:06.445455-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-16T13:35:06.443919-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260416144006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260416144006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260416144006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260416144006)

</details>
