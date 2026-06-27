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
1. `AKUN-001-UNKNOWN-VLESS-WS-106MS` (url=276ms, nekobox=270ms, status=yes)
2. `AKUN-002-CLOUDWEBMANAGE-EU-FR-VLESS-WS-113MS` (url=284ms, nekobox=337ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-137MS` (url=287ms, nekobox=300ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-123MS` (url=289ms, nekobox=323ms, status=yes)
5. `AKUN-005-466688-VLESS-WS-138MS` (url=276ms, nekobox=308ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-130MS` (url=299ms, nekobox=345ms, status=yes)
7. `AKUN-007-COMPREND-NET-VLESS-WS-101MS` (url=270ms, nekobox=294ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-120MS` (url=248ms, nekobox=315ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-138MS` (url=244ms, nekobox=309ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-139MS` (url=250ms, nekobox=350ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-129MS` (url=280ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-133MS` (url=238ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-168MS` (url=252ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-142MS` (url=296ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-120MS` (url=255ms, status=HTTP 204)
16. `AKUN-016-SPEEDTEST-VLESS-WS-157MS` (url=264ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-145MS` (url=273ms, status=HTTP 204)
18. `AKUN-018-SPEEDTEST-VLESS-WS-304MS` (url=918ms, status=HTTP 204)
19. `AKUN-019-SPEEDTEST-VLESS-WS-289MS` (url=664ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-305MS` (url=2715ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-105MS` (url=351ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-328MS` (url=694ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-343MS` (url=685ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-347MS` (url=702ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-272MS` (url=470ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
