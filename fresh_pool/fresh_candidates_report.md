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
1. `AKUN-001-UNKNOWN-VLESS-WS-92MS` (url=211ms, nekobox=231ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-83MS` (url=296ms, nekobox=252ms, status=yes)
3. `AKUN-003-APPLESERAJ-VLESS-WS-109MS` (url=225ms, nekobox=228ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-112MS`
5. `AKUN-004-UNKNOWN-VLESS-WS-88MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-120MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-96MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-254MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-260MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-293MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-226MS`
12. `AKUN-013-CLOUDFLARE-VLESS-WS-276MS` (url=644ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-249MS` (url=524ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-352MS` (url=681ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-366MS` (url=648ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-132MS` (url=284ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-372MS` (url=662ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-391MS` (url=663ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-390MS` (url=693ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-369MS` (url=668ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-271MS` (url=597ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-364MS` (url=703ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-396MS` (url=1544ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-382MS` (url=1889ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-366MS` (url=697ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
