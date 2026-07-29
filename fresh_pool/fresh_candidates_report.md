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
1. `AKUN-001-BIGCOMMERCE-VLESS-WS-65MS` (url=204ms, nekobox=228ms, status=yes)
2. `AKUN-002-ES-FORNEX-20160629-VLESS-WS-65MS` (url=233ms, nekobox=239ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-66MS` (url=224ms, nekobox=171ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-62MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-91MS`
6. `AKUN-007-CLOUDFLARE-VLESS-WS-82MS` (url=196ms, nekobox=174ms, status=no)
7. `AKUN-008-CLOUDFLARE-VLESS-WS-88MS` (url=215ms, nekobox=185ms, status=no)
8. `AKUN-005-UNKNOWN-VLESS-WS-66MS`
9. `AKUN-006-UNKNOWN-VLESS-WS-103MS`
10. `AKUN-007-UNKNOWN-VLESS-WS-111MS`
11. `AKUN-008-CLOUDFLARE-VLESS-WS-126MS`
12. `AKUN-009-CLOUDFLARE-VLESS-WS-65MS`
13. `AKUN-010-CLOUDFLARE-VLESS-WS-132MS`
14. `AKUN-016-CLOUDFLARE-VLESS-WS-147MS` (url=215ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-162MS` (url=209ms, status=HTTP 204)
16. `AKUN-018-UNKNOWN-VLESS-WS-188MS` (url=273ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-59MS` (url=212ms, status=HTTP 204)
18. `AKUN-020-MEDIUM-VLESS-WS-62MS` (url=204ms, status=HTTP 204)
19. `AKUN-021-TANG-NET-VLESS-WS-234MS` (url=495ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-216MS` (url=471ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-405MS` (url=689ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-63MS` (url=210ms, status=HTTP 204)
23. `AKUN-028-ZABIDAT-VLESS-WS-452MS` (url=952ms, status=HTTP 204)
24. `AKUN-029-CLOUDFLARE-VLESS-WS-451MS` (url=795ms, status=HTTP 204)
25. `AKUN-032-CLOUDFLARE-VLESS-WS-548MS` (url=1079ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
