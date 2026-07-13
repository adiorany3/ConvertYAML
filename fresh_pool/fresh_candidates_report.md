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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-UNKNOWN-VLESS-WS-92MS` (url=373ms, nekobox=362ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-111MS` (url=316ms, nekobox=313ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-114MS` (url=305ms, nekobox=319ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-119MS` (url=283ms, nekobox=346ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-120MS` (url=267ms, nekobox=402ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-123MS` (url=321ms, nekobox=328ms, status=yes)
7. `AKUN-007-DEV-VLESS-WS-120MS` (url=324ms, nekobox=235ms, status=no)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-129MS` (url=302ms, nekobox=227ms, status=no)
9. `AKUN-007-UNKNOWN-VLESS-WS-110MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-131MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-123MS`
12. `AKUN-010-466688-VLESS-WS-134MS`
13. `AKUN-013-UNKNOWN-VLESS-WS-117MS` (url=308ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-131MS` (url=301ms, status=HTTP 204)
15. `AKUN-015-ZVC-VLESS-WS-123MS` (url=303ms, status=HTTP 204)
16. `AKUN-016-466688-VLESS-WS-126MS` (url=390ms, status=HTTP 204)
17. `AKUN-017-HETZNER-VLESS-WS-136MS` (url=323ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-131MS` (url=298ms, status=HTTP 204)
19. `AKUN-019-HETZNER-VLESS-WS-170MS` (url=393ms, status=HTTP 204)
20. `AKUN-020-PUBLICDOMAINREGISTRY-NET-VLESS-WS-119MS` (url=301ms, status=HTTP 204)
21. `AKUN-021-US-VLESS-WS-162MS` (url=307ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-135MS` (url=296ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-272MS` (url=702ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-287MS` (url=2921ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-320MS` (url=736ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
