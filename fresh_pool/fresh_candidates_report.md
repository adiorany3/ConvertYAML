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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-88MS` (url=900ms, nekobox=231ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-92MS` (url=207ms, nekobox=237ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-90MS` (url=207ms, nekobox=241ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-89MS` (url=220ms, nekobox=241ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-94MS` (url=227ms, nekobox=258ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-93MS` (url=211ms, nekobox=239ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-106MS` (url=200ms, nekobox=236ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-92MS` (url=210ms, nekobox=261ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-103MS` (url=199ms, nekobox=241ms, status=yes)
10. `AKUN-010-WPENG-VLESS-WS-116MS` (url=205ms, nekobox=225ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-119MS` (url=225ms, status=HTTP 204)
12. `AKUN-012-ORG-VLESS-WS-96MS` (url=218ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-117MS` (url=223ms, status=HTTP 204)
14. `AKUN-014-ZVC-VLESS-WS-117MS` (url=212ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-111MS` (url=234ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-144MS` (url=204ms, status=HTTP 204)
17. `AKUN-017-UK-GB-DCL-01-20191003-VLESS-WS-114MS` (url=224ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-139MS` (url=229ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-134MS` (url=280ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-158MS` (url=225ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-153MS` (url=233ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-146MS` (url=253ms, status=HTTP 204)
23. `AKUN-023-DE5-VLESS-WS-113MS` (url=256ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-127MS` (url=250ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-134MS` (url=250ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
