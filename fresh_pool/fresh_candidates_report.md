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
1. `AKUN-001-UNKNOWN-VLESS-WS-68MS` (url=240ms, nekobox=270ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-61MS` (url=243ms, nekobox=281ms, status=yes)
3. `AKUN-003-COMPREND-NET-VLESS-WS-83MS` (url=234ms, nekobox=275ms, status=yes)
4. `AKUN-004-COMPREND-NET-VLESS-WS-80MS` (url=259ms, nekobox=264ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-84MS` (url=228ms, nekobox=273ms, status=yes)
6. `AKUN-006-COMPREND-NET-VLESS-WS-122MS` (url=267ms, nekobox=265ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-92MS`
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-134MS`
9. `AKUN-009-UNKNOWN-VLESS-WS-84MS`
10. `AKUN-010-466688-VLESS-WS-70MS`
11. `AKUN-013-CLOUDFLARE-VLESS-WS-83MS` (url=232ms, status=HTTP 204)
12. `AKUN-014-CLOUDFLARE-VLESS-WS-288MS` (url=620ms, status=HTTP 204)
13. `AKUN-015-UNKNOWN-VLESS-WS-293MS` (url=708ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-311MS` (url=672ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-262MS` (url=601ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-311MS` (url=690ms, status=HTTP 204)
17. `AKUN-019-UK-GB-DCL-01-20191003-VLESS-WS-89MS` (url=295ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-349MS` (url=581ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-252MS` (url=554ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-80MS` (url=267ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-295MS` (url=609ms, status=HTTP 204)
22. `AKUN-024-CCTVHIKVISION-VLESS-WS-480MS` (url=775ms, status=HTTP 204)
23. `AKUN-028-RC-PRO-5-VLESS-WS-499MS` (url=900ms, status=HTTP 204)
24. `AKUN-029-RS-RAPIDSEEDBOX-20190717-VLESS-WS-537MS` (url=919ms, status=HTTP 204)
25. `AKUN-031-UNKNOWN-VLESS-WS-643MS` (url=947ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
