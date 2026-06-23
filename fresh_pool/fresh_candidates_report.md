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
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-UNKNOWN-VLESS-WS-61MS` (url=240ms, nekobox=241ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-86MS` (url=206ms, nekobox=179ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-70MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-93MS` (url=229ms, nekobox=194ms, status=no)
5. `AKUN-003-CLOUDFLARE-VLESS-WS-91MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-73MS` (url=228ms, nekobox=188ms, status=no)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-98MS` (url=224ms, nekobox=221ms, status=no)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-105MS` (url=223ms, nekobox=186ms, status=no)
9. `AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-86MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-74MS` (url=222ms, nekobox=191ms, status=no)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-96MS` (url=200ms, nekobox=180ms, status=no)
12. `AKUN-012-UNKNOWN-VLESS-WS-101MS` (url=225ms, nekobox=179ms, status=no)
13. `AKUN-005-UNKNOWN-VLESS-WS-92MS`
14. `AKUN-006-UNKNOWN-VLESS-WS-80MS`
15. `AKUN-007-UNKNOWN-VLESS-WS-112MS`
16. `AKUN-008-UNKNOWN-VLESS-WS-97MS`
17. `AKUN-009-UNKNOWN-VLESS-WS-83MS`
18. `AKUN-010-CLOUDFLARE-VLESS-WS-234MS`
19. `AKUN-019-UNKNOWN-VLESS-WS-250MS` (url=547ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-255MS` (url=543ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-251MS` (url=604ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-275MS` (url=586ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-229MS` (url=503ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-236MS` (url=631ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-446MS` (url=699ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
