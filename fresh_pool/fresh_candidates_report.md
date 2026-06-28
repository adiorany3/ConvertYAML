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
1. `AKUN-001-9889888-VLESS-WS-68MS` (url=215ms, nekobox=242ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-70MS` (url=201ms, nekobox=233ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-80MS` (url=209ms, nekobox=246ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-65MS` (url=206ms, nekobox=230ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-97MS` (url=215ms, nekobox=240ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-90MS` (url=218ms, nekobox=227ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-91MS` (url=232ms, nekobox=248ms, status=yes)
8. `AKUN-008-US-VLESS-WS-98MS` (url=213ms, nekobox=246ms, status=yes)
9. `AKUN-009-COMPREND-NET-VLESS-WS-77MS` (url=202ms, nekobox=230ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-90MS` (url=228ms, nekobox=229ms, status=yes)
11. `AKUN-011-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-68MS` (url=207ms, status=HTTP 204)
12. `AKUN-012-ZOOM-VLESS-WS-116MS` (url=209ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-84MS` (url=206ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-112MS` (url=215ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-248MS` (url=5003ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-234MS` (url=505ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-256MS` (url=555ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-263MS` (url=611ms, status=HTTP 204)
19. `AKUN-019-COMPREND-NET-VLESS-WS-76MS` (url=200ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-274MS` (url=551ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-268MS` (url=584ms, status=HTTP 204)
22. `AKUN-022-RS-RAPIDSEEDBOX-20190717-VLESS-WS-253MS` (url=687ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-235MS` (url=494ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-317MS` (url=566ms, status=HTTP 204)
25. `AKUN-027-UK-GB-DCL-01-20191003-VLESS-WS-178MS` (url=354ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
