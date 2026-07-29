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
1. `AKUN-001-LEVIKOGJGFDD-VLESS-WS-61MS` (url=234ms, nekobox=303ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-59MS` (url=231ms, nekobox=270ms, status=yes)
3. `AKUN-003-DEV-VLESS-WS-67MS` (url=223ms, nekobox=328ms, status=yes)
4. `AKUN-004-SPEEDTEST-VLESS-WS-85MS` (url=245ms, nekobox=177ms, status=no)
5. `AKUN-004-UNKNOWN-VLESS-WS-70MS`
6. `AKUN-005-ZVC-VLESS-WS-85MS`
7. `AKUN-006-HOSTINGER-VLESS-WS-82MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-74MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-93MS`
10. `AKUN-009-DEV-VLESS-WS-107MS`
11. `AKUN-011-SPEEDTEST-VLESS-WS-120MS` (url=239ms, nekobox=174ms, status=no)
12. `AKUN-010-CLOUDFLARE-VLESS-WS-84MS`
13. `AKUN-013-UNKNOWN-VLESS-WS-95MS` (url=218ms, status=HTTP 204)
14. `AKUN-014-EU-VLESS-WS-111MS` (url=223ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-118MS` (url=288ms, status=HTTP 204)
16. `AKUN-017-ZOOM-VLESS-WS-144MS` (url=223ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-114MS` (url=243ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-116MS` (url=218ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-68MS` (url=302ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-157MS` (url=370ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-218MS` (url=275ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-76MS` (url=267ms, status=HTTP 204)
23. `AKUN-024-LEVIKOGJGFDD-VLESS-WS-245MS` (url=527ms, status=HTTP 204)
24. `AKUN-025-CONFLU-VLESS-WS-246MS` (url=549ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-424MS` (url=706ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
