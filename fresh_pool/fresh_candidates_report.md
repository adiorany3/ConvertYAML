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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-103MS` (url=228ms, nekobox=249ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-90MS` (url=255ms, nekobox=259ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-107MS` (url=223ms, nekobox=260ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-106MS` (url=232ms, nekobox=264ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-102MS` (url=259ms, nekobox=274ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-117MS` (url=224ms, nekobox=246ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-110MS` (url=250ms, nekobox=284ms, status=yes)
8. `AKUN-008-090227-VLESS-WS-121MS` (url=238ms, nekobox=264ms, status=yes)
9. `AKUN-009-MEDIUM-VLESS-WS-139MS` (url=238ms, nekobox=265ms, status=yes)
10. `AKUN-010-DEV-VLESS-WS-138MS` (url=217ms, nekobox=209ms, status=no)
11. `AKUN-010-UNKNOWN-VLESS-WS-133MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-138MS` (url=244ms, status=HTTP 204)
13. `AKUN-013-1PASSWORD-VLESS-WS-126MS` (url=247ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-107MS` (url=236ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-111MS` (url=261ms, status=HTTP 204)
16. `AKUN-016-COMPREND-NET-VLESS-WS-115MS` (url=228ms, status=HTTP 204)
17. `AKUN-017-ADF-VLESS-WS-124MS` (url=243ms, status=HTTP 204)
18. `AKUN-018-COMPREND-NET-VLESS-WS-138MS` (url=233ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-153MS` (url=227ms, status=HTTP 204)
20. `AKUN-020-COMPREND-NET-VLESS-WS-134MS` (url=221ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-236MS` (url=434ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-207MS` (url=289ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-192MS` (url=254ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-332MS` (url=664ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-332MS` (url=657ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
