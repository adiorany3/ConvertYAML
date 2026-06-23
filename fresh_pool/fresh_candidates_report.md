# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 15
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 21

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-UK-GB-DCL-01-20191003-VLESS-WS-81MS` (url=267ms, nekobox=226ms, status=yes)
2. `AKUN-002-ORACLE-VLESS-WS-84MS` (url=222ms, nekobox=252ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-91MS` (url=240ms, nekobox=196ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-95MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-94MS`
6. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-74MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-244MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-249MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-241MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-247MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-271MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-263MS` (url=563ms, status=HTTP 204)
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-258MS` (url=551ms, status=HTTP 204)
14. `AKUN-026-UNKNOWN-VLESS-WS-475MS` (url=749ms, status=HTTP 204)
15. `AKUN-030-UNKNOWN-VLESS-WS-581MS` (url=1056ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
