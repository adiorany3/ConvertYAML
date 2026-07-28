# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-56MS` (url=218ms, nekobox=242ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-57MS` (url=227ms, nekobox=248ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-69MS` (url=214ms, nekobox=242ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-58MS` (url=209ms, nekobox=236ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-65MS` (url=197ms, nekobox=248ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-64MS` (url=223ms, nekobox=245ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-64MS` (url=216ms, nekobox=242ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-79MS` (url=243ms, nekobox=277ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-77MS` (url=226ms, nekobox=170ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-72MS` (url=201ms, nekobox=172ms, status=no)
12. `AKUN-010-UNKNOWN-VLESS-WS-110MS`
13. `AKUN-015-UNKNOWN-VLESS-WS-61MS` (url=191ms, status=HTTP 204)
14. `AKUN-016-UNKNOWN-VLESS-WS-82MS` (url=217ms, status=HTTP 204)
15. `AKUN-017-EU-VLESS-WS-103MS` (url=215ms, status=HTTP 204)
16. `AKUN-018-UNKNOWN-VLESS-WS-81MS` (url=208ms, status=HTTP 204)
17. `AKUN-019-UNKNOWN-VLESS-WS-127MS` (url=230ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-125MS` (url=212ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-87MS` (url=234ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-95MS` (url=220ms, status=HTTP 204)
21. `AKUN-023-090227-VLESS-WS-295MS` (url=624ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-339MS` (url=725ms, status=HTTP 204)
23. `AKUN-026-SUKARIO-VLESS-WS-653MS` (url=1108ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-677MS` (url=1166ms, status=HTTP 204)
25. `AKUN-030-UNKNOWN-VLESS-WS-766MS` (url=1236ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
