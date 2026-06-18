# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 20
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 26

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS` (url=201ms, nekobox=248ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-83MS` (url=203ms, nekobox=249ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=219ms, nekobox=248ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-78MS` (url=231ms, nekobox=241ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-88MS` (url=231ms, nekobox=187ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-85MS`
7. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-98MS`
8. `AKUN-007-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-104MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-133MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-92MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-222MS`
12. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-134MS` (url=222ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-208MS` (url=203ms, status=HTTP 204)
14. `AKUN-016-UNKNOWN-VLESS-WS-271MS` (url=540ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-250MS` (url=551ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-262MS` (url=490ms, status=HTTP 204)
17. `AKUN-019-MICROSOFT-VLESS-WS-286MS` (url=558ms, status=HTTP 204)
18. `AKUN-021-CLOUDFLARE-VLESS-WS-298MS` (url=2439ms, status=HTTP 204)
19. `AKUN-024-CLOUDFLARE-VLESS-WS-259MS` (url=548ms, status=HTTP 204)
20. `AKUN-025-IRATOM-VLESS-WS-400MS` (url=600ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
